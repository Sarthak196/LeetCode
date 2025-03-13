import heapq
def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []
    visited, heap, res = set(), [], []
    heapq.heappush(heap, ((nums1[0]+nums2[0]), 0, 0)) # create a heap with sum of 0th element of nums1 and nums2
    visited.add([0,0]) # add 0th indexes into visited list so that we do not re-visit it again
    while len(res)<k and heap:
        s, i, j = heapq.heappop(heap) # always pops out the element with minimum sum as sum is the 1st parameter in our heap
        res.append([nums1[i], nums2[j]]) # append the elements into the list
        if i+1 < len(nums1) and (i+1, j) not in visited: #search for i+1 and j index
            heapq.heappush(heap, ((nums1[i+1] + nums2[j]), i+1, j))
            visited.add([i+1, j])
        if j+1 < len(nums2) and (i, j+1) not in visited: # search for j+1 and i index
            heapq.heappush(heap, ((nums1[i]+nums2[j+1]), i, j+1))
            visited.add([i, j+1])
    return res


nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(kSmallestPairs(nums1, nums2, k)) #[[1,1],[1,1]]