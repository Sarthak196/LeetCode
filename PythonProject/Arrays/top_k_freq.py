def topKFrequent(nums, k):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    x = [v for v in d.values()]
    x.sort(reverse=True)
    buckets = [[]*i for i in range(x[0] + 1)] #bucket sort
    for i in nums:
        buckets[d[i]].append(i)
    final_list = []
    for i in range(len(buckets) - 1, -1, -1):
        final_list.append(list(set(buckets[i])))
    result = []
    for i in final_list:
        for j in i:
            result.append(j)
    return result[:k]

nums = [1,1,2,2,2,3,3,3,3,4,4,4,4]
k = 3
print(topKFrequent(nums, k)) # [3, 4, 2]

# Create a dictionary to store the count of each number. Create a list of the values of the dictionary and sort it in
# reverse order. Create a list of lists called buckets with the length of the maximum value in the dictionary + 1.
# Iterate through the numbers and append the number to the bucket at the index of the count of the number. This is
# called bucket sort. Create a list called final_list and iterate through the buckets in reverse order and append the
# unique elements of the bucket to the final_list. Finally, iterate through the final_list and append the elements to
# the result list and return the first k elements of the result list.
