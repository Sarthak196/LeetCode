def longestPalindrome(s):
    res = ''
    maxlen = 0

    def checkPalindrome(left, right):
        while left>=0 and right<len(s) and s[left]==s[right]: # if char at left and right are same
            left-=1 # take a point as center and expand both left and right
            right+=1
        return s[left+1: right] # left+1 and right is given because the while loop can break when l= -1 and right > len(s)

    for i in range(len(s)):
        odd =  checkPalindrome(i,i) # odd has a single mid point
        even = checkPalindrome(i, i+1) # even will have 2 mid points
        if len(odd) > maxlen: # keep updating res and maxlen
            res = odd
            maxlen = len(odd)
        if len(even) > maxlen:
            res = even
            maxlen = len(even)
    return res

s = "babad"
print(longestPalindrome(s))