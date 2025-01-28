def characterReplacement(s, k):
    d = {}
    l, res = 0, 0
    for r in range(len(s)): # r is the right pointer
        d[s[r]] = 1 + d.get(s[r], 0) # d is the dictionary to store the count of each character
        while (r - l + 1) - max(d.values()) > k: # if the number of characters to be replaced is greater than k
            d[s[l]] -= 1 # decrease the count of the character at the left pointer
            l += 1 # move the left pointer to the right
        res = max(res, (r - l + 1)) # update the result
    return res
s="AABABBA"
k=1
print(characterReplacement(s, k)) # 4

# we always replace the characters with the least frequent character in the window with the most frequent character