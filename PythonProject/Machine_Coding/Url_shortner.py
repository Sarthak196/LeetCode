"""
Functional req:
    1. Shorten URL - Given a long URL, generate a unique short URL
    2. Redirect to original URL when short URL is accessed
    3. Handle edge cases (invalid URLs, duplicate URLs, etc.)

Non-functional req:
    1. Minimize latency for URL redirection
    2. Scalability to handle a large number of URLs
    3. 1B reads per day, 10k requests per second
    4. Hold maybe 5 billion URLs in the system

Design:
    1. POST /shorten - to shorten a URL and return the short URL
    2. GET /{short_url} - to redirect to the original URL, redirect 302
"""

import hashlib
import time
from typing import Optional, Dict, Tuple
from datetime import datetime, timedelta
import string
import random


class URLShortener:
    """
    URL Shortener system that converts long URLs to short, unique codes.
    
    Approach:
    - Use base62 encoding for short codes (0-9, a-z, A-Z = 62 characters)
    - Use counter + random component for uniqueness
    - Store mappings in memory with TTL support
    - Use hash to detect duplicate URLs
    """
    
    # Characters for base62 encoding
    BASE62_CHARS = string.digits + string.ascii_lowercase + string.ascii_uppercase
    
    def __init__(self, base_url: str = "http://short.url/", ttl_days: int = 365):
        """
        Initialize URL Shortener.
        
        Args:
            base_url: Base URL for shortened links
            ttl_days: Time to live for each shortened URL in days
        """
        self.base_url = base_url
        self.ttl_days = ttl_days
        
        # Mappings: short_code -> (long_url, creation_time, access_count)
        self.short_to_long: Dict[str, Tuple[str, float, int]] = {}
        
        # Reverse mapping for deduplication: hash(long_url) -> short_code
        self.long_to_short: Dict[str, str] = {}
        
        # Counter for generating unique codes
        self.counter = 0
        
    def _hash_url(self, url: str) -> str:
        """Generate a hash of the URL for deduplication."""
        return hashlib.md5(url.encode()).hexdigest()
    
    def _is_valid_url(self, url: str) -> bool:
        """Validate URL format."""
        if not isinstance(url, str):
            return False
        if not url.startswith(('http://', 'https://')):
            return False
        if len(url) < 10:
            return False
        return True
    
    def _is_expired(self, short_code: str) -> bool:
        """Check if a short code has expired."""
        if short_code not in self.short_to_long:
            return True
        
        long_url, creation_time, _ = self.short_to_long[short_code]
        expiry_time = creation_time + (self.ttl_days * 24 * 3600)
        return time.time() > expiry_time
    
    def _generate_short_code(self) -> str:
        """
        Generate a unique short code using counter and random component.
        Counter ensures uniqueness, random component adds security.
        """
        self.counter += 1
        
        # Combine counter with timestamp and random value
        unique_value = self.counter + int(time.time() * 1000000) + random.randint(0, 999999)
        
        # Convert to base62
        short_code = self._encode_base62(unique_value)
        
        # Ensure minimum length of 6-8 characters for readability
        while len(short_code) < 6:
            short_code = random.choice(self.BASE62_CHARS) + short_code
        
        return short_code[:8]  # Cap at 8 characters for short URLs
    
    def _encode_base62(self, num: int) -> str:
        """Convert a number to base62 string."""
        if num == 0:
            return self.BASE62_CHARS[0]
        
        chars = []
        while num > 0:
            chars.append(self.BASE62_CHARS[num % 62])
            num //= 62
        
        return ''.join(reversed(chars))
    
    def _decode_base62(self, s: str) -> int:
        """Convert a base62 string to a number."""
        num = 0
        for char in s:
            num = num * 62 + self.BASE62_CHARS.index(char)
        return num
    
    def shorten(self, long_url: str, custom_short: Optional[str] = None) -> Optional[str]:
        """
        Shorten a long URL.
        
        Args:
            long_url: The original URL to shorten
            custom_short: Optional custom short code
            
        Returns:
            Short URL or None if invalid input
        """
        # Validate URL
        if not self._is_valid_url(long_url):
            print(f"Invalid URL: {long_url}")
            return None
        
        # Check for duplicates
        url_hash = self._hash_url(long_url)
        if url_hash in self.long_to_short:
            short_code = self.long_to_short[url_hash]
            if not self._is_expired(short_code):
                print(f"URL already shortened: {self.base_url}{short_code}")
                return self.base_url + short_code
            else:
                # Remove expired entry
                del self.short_to_long[short_code]
                del self.long_to_short[url_hash]
        
        # Use custom short code if provided
        if custom_short:
            if len(custom_short) < 2:
                print("Custom short code must be at least 2 characters")
                return None
            if custom_short in self.short_to_long and not self._is_expired(custom_short):
                print(f"Custom short code already in use: {custom_short}")
                return None
            short_code = custom_short
        else:
            # Generate short code
            short_code = self._generate_short_code()
            while short_code in self.short_to_long and not self._is_expired(short_code):
                short_code = self._generate_short_code()
        
        # Store mappings
        self.short_to_long[short_code] = (long_url, time.time(), 0)
        self.long_to_short[url_hash] = short_code
        
        return self.base_url + short_code
    
    def expand(self, short_code: str) -> Optional[str]:
        """
        Expand a short code back to the original long URL.
        
        Args:
            short_code: The short code (with or without base URL)
            
        Returns:
            Original long URL or None if not found or expired
        """
        # Extract just the code if full URL is provided
        if short_code.startswith(self.base_url):
            short_code = short_code[len(self.base_url):]
        
        # Check if code exists and not expired
        if short_code not in self.short_to_long:
            print(f"Short code not found: {short_code}")
            return None
        
        if self._is_expired(short_code):
            print(f"Short code has expired: {short_code}")
            del self.short_to_long[short_code]
            return None
        
        # Update access count
        long_url, creation_time, access_count = self.short_to_long[short_code]
        self.short_to_long[short_code] = (long_url, creation_time, access_count + 1)
        
        return long_url
    
    def get_stats(self, short_code: str) -> Optional[Dict]:
        """Get statistics for a shortened URL."""
        if short_code.startswith(self.base_url):
            short_code = short_code[len(self.base_url):]
        
        if short_code not in self.short_to_long:
            return None
        
        long_url, creation_time, access_count = self.short_to_long[short_code]
        
        return {
            'short_code': short_code,
            'long_url': long_url,
            'created_at': datetime.fromtimestamp(creation_time).isoformat(),
            'access_count': access_count,
            'is_expired': self._is_expired(short_code)
        }
    
    def delete(self, short_code: str) -> bool:
        """Delete a shortened URL."""
        if short_code.startswith(self.base_url):
            short_code = short_code[len(self.base_url):]
        
        if short_code in self.short_to_long:
            long_url, _, _ = self.short_to_long[short_code]
            url_hash = self._hash_url(long_url)
            
            del self.short_to_long[short_code]
            if url_hash in self.long_to_short:
                del self.long_to_short[url_hash]
            return True
        return False


# ============= Demo / Testing =============
if __name__ == "__main__":
    shortener = URLShortener(base_url="http://short.url/")
    
    print("=" * 60)
    print("URL SHORTENER DEMO")
    print("=" * 60)
    
    # Test 1: Shorten a URL
    print("\n1. Testing URL shortening:")
    url1 = "https://www.github.com/torvalds/linux"
    short1 = shortener.shorten(url1)
    print(f"Original: {url1}")
    print(f"Shortened: {short1}")
    
    # Test 2: Duplicate URL (should return same short code)
    print("\n2. Testing duplicate URL:")
    short1_dup = shortener.shorten(url1)
    print(f"Shortened again: {short1_dup}")
    print(f"Same as before: {short1 == short1_dup}")
    
    # Test 3: Custom short code
    print("\n3. Testing custom short code:")
    url2 = "https://stackoverflow.com/questions/tagged/python"
    short2 = shortener.shorten(url2, custom_short="python")
    print(f"Original: {url2}")
    print(f"Custom shortened: {short2}")
    
    # Test 4: Expand short URL
    print("\n4. Testing URL expansion:")
    expanded = shortener.expand(short1)
    print(f"Expanded from {short1}")
    print(f"Result: {expanded}")
    
    # Test 5: Get stats
    print("\n5. Testing URL statistics:")
    stats = shortener.get_stats(short1)
    if stats:
        print(f"Short Code: {stats['short_code']}")
        print(f"Original URL: {stats['long_url']}")
        print(f"Created at: {stats['created_at']}")
        print(f"Access count: {stats['access_count']}")
        print(f"Expired: {stats['is_expired']}")
    
    # Test 6: Multiple accesses
    print("\n6. Testing multiple accesses:")
    shortener.expand(short1)
    shortener.expand(short1)
    stats = shortener.get_stats(short1)
    print(f"Access count after 3 total accesses: {stats['access_count']}")
    
    # Test 7: Invalid URL
    print("\n7. Testing invalid URL:")
    invalid = shortener.shorten("not-a-url")
    print(f"Result for invalid URL: {invalid}")
    
    # Test 8: Delete
    print("\n8. Testing URL deletion:")
    print(f"Before deletion - expanded: {shortener.expand(short2)}")
    deleted = shortener.delete(short2)
    print(f"Deleted: {deleted}")
    print(f"After deletion - expanded: {shortener.expand(short2)}")
    
    print("\n" + "=" * 60)