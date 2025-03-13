def merge_sort(nums):
    if len(nums)>1:
        mid = len(nums)//2 # divide the array into two halves continuously until just a single element remains
        lefthalf = nums[:mid]
        righthalf = nums[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0 # pointers for lefthalf, righthalf and original array
        while i<len(lefthalf) and j < len(righthalf): # comapre and insert the sortest element
            if lefthalf[i] < righthalf[j]:
                nums[k] = lefthalf[i]
                i+=1
            else:
                nums[k] = righthalf[j]
                j+=1
            k+=1
        while i<len(lefthalf):
            nums[k] = lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            nums[k] = righthalf[j]
            j+=1
            k+=1
    return nums



nums = [3,2,66,45,12,1,3]
print(merge_sort(nums))# [1, 2, 3, 3, 12, 45, 66]

# time complexity: o(nlogn)