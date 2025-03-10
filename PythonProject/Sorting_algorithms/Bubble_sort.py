def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1): # everytime in bubble sort the largest element will get sorted 1st hence we do
                                        # only n-1 passes
        for j in range(i): # j runs till i, as after i everything is sorted
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] # swap if current index is larger that current index+1
    return nums

nums = [3,2,66,45,12,1,3]
print(bubble_sort(nums))# [1, 2, 3, 3, 12, 45, 66]

# in bubble sort, sorting is done in pairs.