def permute(nums):
    def recursive(nums, perm=[], res=[]):

        if not nums:
            res.append(perm)  # if list is empty, return [[]]

        for i in range(len(nums)):
            newNums = nums[:i] + nums[i + 1:] # take rest of the number except at ith pos
            newPerm = perm + [nums[i]]  # keep updating the prem as nums keep changing with newNums
            recursive(newNums, newPerm, res)
        return res

    return recursive(nums)

print(permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]