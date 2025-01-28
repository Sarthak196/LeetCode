def checkInclusion(s1, s2):
    window = []
    l = 0
    length = len(s1)
    list_s1 = [c for c in s1]
    list_s1.sort()
    if sorted(s2) == list_s1: # if s2 is already a permutation of s1 return True
        return True
    for r in range(len(s2)):
        if (r - l + 1) <= length: # if the window size is less than the length of s1
            window.append(s2[r]) # add the character to the window
        else:
            if sorted(window) == list_s1: # if the window is a permutation of s1 return true
                return True
            window.pop(0) # remove the first element from the window
            l += 1 # move the left pointer to the right
            window.append(s2[r]) # add the right character to the window
            if sorted(window) == list_s1: # if the window is a permutation of s1 return true
                return True
    return False

s1 = "ab"
s2 = "ba"
print(checkInclusion(s1, s2)) # True