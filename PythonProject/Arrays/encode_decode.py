def encode(strs):
    res = ""
    for c in strs:
        res += str(len(c)) + '#' + c
    return res


def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1 # j stops when ever # occurs
        length = int(s[i:j]) # length of the string
        i = j + 1 # skip the # and start i
        j = i + length  # j stops at the end of the string
        res.append(s[i:j]) # append the string to the result
        i = j # start i at the end of the string or before the next number
    return res


strs =  ["we","say",":","yes","!@#$%^&*()"]
s = encode(strs)
print(s) # 2#we3#say1#:3#yes10#!@#$%^&*()
print(decode(s))