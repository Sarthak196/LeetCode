def shell_sort(nums):
    sublist_len = len(nums)//2
    while sublist_len>0: # break the list into smaller part
        for start in range(sublist_len):
            nums = insertion_sort(nums,start,sublist_len)
        sublist_len = sublist_len//2
    return nums

def insertion_sort(nums, start, gap): # these smaller parts are called as gap
    for i in range(start+gap, len(nums), gap): # start i from start+gap as start starts from 0 and in insertion sort we
                                              # assume that 0th element is always sorted.
        curr_val = nums[i]
        pos = i
        while pos>=gap and nums[pos-gap]>curr_val:
            nums[pos] = nums[pos-gap]
            pos = pos -gap
        nums[pos] = curr_val
    return nums

nums = [3,2,66,45,12,1,3]
print(shell_sort(nums))# [1, 2, 3, 3, 12, 45, 66]

# time complexity: o(nlogn)

# Shell sort is similar to insertion sort. In shell sort we are just breaking that list into smaller parts and applying
# insertion sort on it.