def trap(height):
    maxLeft = [0]
    maxRight = [0]
    x = len(height)
    for l in range(x - 1):
        maxLeft.append(max(height[l], maxLeft[l])) #find the max height to the left of the current index
    for r in range(x - 1, 0, -1):
        maxRight.append(max(height[r], maxRight[x - r - 1])) #find the max height to the right of the current index
    maxRight.reverse() #reverse the right list to get the correct order
    totalVol = 0
    for i in range(x):
        # Formula: min(maxLeft[i], maxRight[i]) - height[i]
        totalVol += max(0, min(maxLeft[i], maxRight[i]) - height[i]) #find the difference between the min of the max
                                                                    # heights to the left and right of the current index
                                                                    # and the current index height
    return totalVol
height = [0,2,0,3,1,0,1,3,2,1]
print(trap(height)) # 9