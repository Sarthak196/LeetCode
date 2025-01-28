def minWindow(s,t):
    if t == "":
        return ""

    countT, window = {}, {} # countT: count of each character in t, window: count of each character in current window
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT) # have: number of characters in t that are in current window, need: number of characters in t
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0) # update window

        if c in countT and window[c] == countT[c]: # if c is in t and the count of c in window is equal to the count of
                                                   # c in t, Then we can update have as one of character count from countT
                                                   # is satisfied
            have += 1

        while have == need: # if all characters in t are in current window
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1 # update result and get it length

            window[s[l]] -= 1 #start poping from left and update window count
            if s[l] in countT and window[s[l]] < countT[s[l]]: # if the count of s[l] in window is less than the count
                                                               # of s[l] in t, decrement have
                have -= 1
            l += 1 # move left pointer
    l, r = res  # get the result window position
    return s[l: r + 1] if resLen != float("infinity") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t)) # "BANC"