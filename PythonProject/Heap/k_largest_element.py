import heapq
def findKthLargest(nums, k):
    heapq.heapify(nums) # create a min heap of nums
    res = heapq.nlargest(k, nums) # use nlargest function to find n elements in descending order
    return res[k-1] # return the element at k-1 index

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k)) # 5