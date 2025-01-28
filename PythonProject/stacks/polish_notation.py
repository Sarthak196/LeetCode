def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i not in ('+', '-', '*', '/'):
            stack.append(int(i))
        elif i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a // b)
    return stack[-1]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))