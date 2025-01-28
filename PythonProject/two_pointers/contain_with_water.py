def maxArea(heights):
    l, r = 0, len(heights) - 1
    maxVol = 0
    while r > l:
        if heights[l] < heights[r]: # move the smaller valued pointer as height always depends on the smaller value
            if (r - l) * min(heights[r], heights[l]) > maxVol:
                maxVol = (r - l) * min(heights[r], heights[l])
            l += 1
        else:
            if (r - l) * min(heights[r], heights[l]) > maxVol:
                maxVol = (r - l) * min(heights[r], heights[l])
            r -= 1
    return maxVol

heights = [1,7,2,5,4,7,3,6]
print(maxArea(heights)) # 35