def rotate(nums, k):
    rotate = k%len(nums) # if k is greater than the length of the array,
                         # we need to take the mod of k with the length of the array
    nums.reverse() # reverse the entire array
    nums[:rotate] = reversed(nums[:rotate]) # reverse the first k elements
    nums[rotate:] = reversed(nums[rotate:]) # reverse the remaining elements
    return nums # return the rotated array

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k)) # [5,6,7,1,2,3,4]