def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1
        else:
            return m
    return -1
nums = [-1, 0, 2, 4, 6, 8]
target = 4
print(search(nums, target))  # 3

# An array should always be sorted in ascending order while performing a binary search on it. Take two pointers l and r
# and initialize them to the start and end of the array, respectively. Calculate the middle index m as (l + r) // 2.
# If the target is less than the middle element, update r to m - 1. If the target is greater than the middle element,
# update l to m + 1. If the target is equal to the middle element, return the index m. If the target is not found, return -1.