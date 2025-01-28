from collections import deque
def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums)-k+1):
        num = nums[i]
        for j in range(i, i+k):
            num = max(num, nums[j])
        res.append(num)
    return res
nums = [1,2,1,0,-1,2,6]
k = 3
print(maxSlidingWindow(nums, k))