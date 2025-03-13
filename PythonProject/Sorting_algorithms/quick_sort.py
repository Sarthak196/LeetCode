def quick_sort(nums):
    quick_sort_help(nums, 0, len(nums)-1) # call another function with array and 1st and last pointers
    return nums

def quick_sort_help(nums, first, last):
    if first<last:
        splitpoint = partition(nums, first, last) # get the spilpoint

        quick_sort_help(nums, first, splitpoint-1) # call the left half
        quick_sort_help(nums, splitpoint+1, last) # call the right half

def partition(nums, first, last):
    pivot = nums[first] # let pivot be the first value
    left = first+1 # left be the index of next element to the pivot
    right = last # right is the last index

    done = False
    while not done:
        while left<=right and nums[left]<=pivot: # always check if right>=left
            left+=1
        while left<=right and nums[right]>=pivot:
            right-=1

        # all the elements on the left must be smaller than pivot and on the right be larger

        if right<left:
            done = True # if right and left cross each other, stop the loop
        else:
            nums[left], nums[right] = nums[right], nums[left] # exchange left and right
    nums[first], nums[right] = nums[right], nums[first] # put the pivot to right as left of the pivot would be sorted
    return right


nums = [3,2,66,45,12,1,3]
print(quick_sort(nums))# [1, 2, 3, 3, 12, 45, 66]

# time complexity: O(n log(n))