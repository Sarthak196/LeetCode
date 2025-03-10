def insertion_sort(nums):
    for i in range(1, len(nums)): # i starts from 1 as we assume that 0th index is already sorted
        curr_val = nums[i]
        pos = i
        while pos>0 and nums[pos-1] > curr_val: # check if previous index is larger than current index
            nums[pos] = nums[pos-1] # change the current pos element with previous element
            pos -=1 # keep going no element previous to the current element is greater
        nums[pos] = curr_val # put the current element in the pos
    return nums

nums = [3,2,66,45,12,1,3]
print(insertion_sort(nums))# [1, 2, 3, 3, 12, 45, 66]

# here we perform n-1 passes and keep inserting the smaller element to the left and larger element to right