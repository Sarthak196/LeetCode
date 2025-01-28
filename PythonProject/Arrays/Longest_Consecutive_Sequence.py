def longestConsecutive(nums):
    d = {} # create a dictionary to store the count of each number and for quick lookup
    for _ in range(len(nums)):
        if nums[_] in d:
            d[nums[_]] += 1
        else:
            d[nums[_]] = 1
    nums = list(set(nums))
    nums.sort() # sort the list of unique numbers
    maxlen = 0
    curlen = 1
    for i in range(len(nums)): # iterate through the list and check if the current number + 1 is in the dictionary
                              # if found then increase the length of the current sequence
        if nums[i] + 1 in d:
            curlen += 1
        else:
            if maxlen <= curlen:
                maxlen = curlen
                curlen = 1
    return maxlen

nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
print(longestConsecutive(nums)) # 4