def findMin(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]: # if the middle index is greater than the right index, # move the left index to the middle
                              # index plus 1. This is because the pivot point is on the right side
            l = m+1
        else: # else move the right index to the middle index because the pivot point is on the left side
            r=m
    pivot =  l
    res = binarySearch(nums, 0, pivot - 1, target) # perform binary search on the left side of the pivot point
    if res!= -1:
        return res
    return binarySearch(nums, pivot, len(nums) - 1, target)
def binarySearch(nums, l, r, target):
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1
nums=[4,5,6,7,0,1,2]
target=0
print(findMin(nums)) # Output 4