def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False
def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        if matrix[i][-1] >= target:
            return search(matrix[i], target)
    return False

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=13
print(searchMatrix(matrix, target))

