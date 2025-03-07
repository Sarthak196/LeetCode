def findMin(nums):
    l, r = 0, len(nums) - 1 # l is the left index and r is the right index
    res = nums[0] # res is the result which is the first element of the array
    while l <= r:
        if nums[l] < nums[r]: # if the left index is less than the right index, return the minimum of the left index and the result
            return min(nums[l], res)
        m = (l + r) // 2 # m is the middle index
        res = min(res, nums[m]) # res is the minimum of the result and the middle index
        if nums[m] >= nums[r]: # if the middle index is greater than or equal to the right index, move the left index to
                                # the middle index plus 1 as the pivot point is on the right side else move the right
                                # index to the middle index minus 1
            l = m + 1
        else:
            r = m - 1
    return res

nums = [4,5,6,7,0,1,2]
print(findMin(nums)) # Output 1
