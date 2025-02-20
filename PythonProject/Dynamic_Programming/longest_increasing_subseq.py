def lengthOfLIS(nums):
    n = len(nums)
    dp = [1]*n # as last elemet will have increasing order of len 1
    for i in range(n-1, -1, -1): # start from last element and move backwards
        for j in range(i+1, n): # start from ith pos and move front
            if nums[i]<nums[j]: # if element after i is greater
                dp[i] = max(dp[i], 1+dp[j]) # add 1 to its length if ith element's length is smaller
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums)) # 4 as [2,3,7,101] or [2,5,7,18] are in increasing order