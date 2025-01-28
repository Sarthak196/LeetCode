def containsDuplicate(nums):
    # dupdict = {}
    # for num in nums:
    #     if num in dupdict:
    #         return True
    #     else:
    #         dupdict[num] = 1
    # return False

    return len(nums) != len(set(nums))
nums = [1, 2, 3]
print(containsDuplicate(nums)) # True

# either use a dictionary to store the count of each number or use a set to store the numbers