def isValid(s):
    pstack = []
    for c in s:
        if c in ('(', '{', '['):
            pstack.append(c) # append only open brackets
        else:
            if pstack: # if stack is not empty, pop the top most corresponding bracket
                if c == '}' and pstack[-1] == '{':
                    pstack.pop()
                elif c == ')' and pstack[-1] == '(':
                    pstack.pop()
                elif c == ']' and pstack[-1] == '[':
                    pstack.pop()
                else:
                    return False
            else:
                return False
    if not pstack: # if stack is empty, return True
        return True
    return False
s = '(])'
print(isValid(s)) # False
