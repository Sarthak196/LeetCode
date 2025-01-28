def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

   # return ''.join(sorted(s)) == ''.join(sorted(t))

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t)) # True

# either sort the string and compare them or use a list to store the count of each character using the ASCII value
# of the character. If the length of the strings are not equal, return False else prepare a list of 26 0s and iterate
# over the strings and increment the count of the character in the first string and decrement the count of the character
# in the second string. If the count list has any non-zero value, return False else return True.