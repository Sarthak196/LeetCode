def selection_sort(nums):
    for i in range(len(nums)-1, 0, -1): # i will start from last index
        postionOfMax = 0 # let postionOfMax be the index of largest element
        for j in range(1, i+1): # j starts from 1 because 0 is assumed to be the index of largest element and goes till
                                # last element
            if nums[j]> nums[postionOfMax]: # changed the index of largest element if bigger element is found
                postionOfMax = j
        nums[i], nums[postionOfMax] = nums[postionOfMax], nums[i] # finally swap the largest element to the last index
    return nums

nums = [3,2,66,45,12,1,3]
print(selection_sort(nums))# [1, 2, 3, 3, 12, 45, 66]

#time complexity: o(n2)

# in selection sort we select the largest element and keep going until we find somthing larger. Finally, we swap the index
# of the large element to the last index