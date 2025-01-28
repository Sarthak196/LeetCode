def is_palindrome(s):
    x = ''.join(c for c in s if c.isalnum()).lower()
    # l = 0
    # r = len(x) - 1
    # while r >= l: # make two pointers l and r to compare the characters from the start and the end
    #     if x[r] != x[l]:
    #         return False
    #     r -= 1
    #     l += 1
    # return True
    if x == x[::-1]:
        return True
    return False

s = "Was it a car or a cat I saw?"
print(is_palindrome(s))  # True