def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        if len(stack) == 0:
            stack.append((t, i)) # put both temperature and the index in the stack
        else:
            while stack and t > stack[-1][0]: # if any larger temperature is found, pop the stack and calculate
                temp, ind = stack.pop()       # the difference between the current index and the popped index and store
                res[ind] = i - ind           # it in the res array at the popped index. Do this until the stack is empty
            stack.append((t, i))            # or the current temperature is less than the temperature at the top of the
    return res                              # stack. Then append the current temperature and index to the stack.
temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))