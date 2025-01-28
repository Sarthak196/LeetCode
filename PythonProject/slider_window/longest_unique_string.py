def lengthOfLongestSubstring(s):
    maxLength, length = 0, 0
    setChar = []
    for r in range(len(s)):
        if s[r] not in setChar: # if the character is not in the list, add it to the list
            setChar.append(s[r])
            length += 1 # increment the length
            maxLength = max(maxLength, length)
        else:
            while s[r] in setChar: # if the character is in the list, remove the first element of the list until the
                                    # character is not in the list
                setChar.pop(0)
                length -= 1 # also decrement the length as we are removing the first element
            setChar.append(s[r])
            length += 1
            maxLength = max(maxLength, length)
    return maxLength

s = "zyxyxza"
print(lengthOfLongestSubstring(s)) # 4