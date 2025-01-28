def twoSum(nums, target):
    dictlookup = {}
    for i, n in enumerate(nums):
        dif = target - n
        if dif in dictlookup:
            return [dictlookup[dif], i]
        dictlookup[n] = i
nums = [1,2,3,4,5]
target = 7
print(twoSum(nums, target)) # [0, 1]

# iterate over the list and enumerate it. Always find the difference between the target and the number and check if the
# difference is already present in the dictionary. If it is present, return the index of the difference and the current
# index.