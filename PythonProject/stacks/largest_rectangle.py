def largestRectangleArea(heights):
    stack = []
    maxArea = 0
    for i in range(len(heights)):
        if not stack:
            stack.append((i, heights[i]))
        else:
            if heights[i] < stack[-1][1]:
                    while stack and heights[i] < stack[-1][1]:
                        ind, h = stack.pop()
                        if ((i - ind) * h) > maxArea:
                            maxArea = ((i - ind) * h)
                    stack.append((ind, heights[i]))
            else:
                stack.append((i, heights[i]))
    while stack:
        ind, h = stack.pop()
        if ((len(heights) - ind) * h) > maxArea:
            maxArea = ((len(heights) - ind) * h)
    return maxArea
heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))

# explaination: https://www.youtube.com/watch?v=zx5Sw9130L0