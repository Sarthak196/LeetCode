def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n # create a dp array of size n with all elements as 0
    dp[0] = nums[0] # set the first element of dp as the first element of nums
    dp[1] = max(nums[0], nums[1]) # set the second element of dp as the max of first and second element of nums
    for i in range(2, n): # iterate from 2 to n so that i-2 will not go in negative
        dp[i] = max(dp[i - 1], (nums[i] + dp[i - 2])) # set the ith element of dp as the max of i-1 and
                                                      # num[i]+ i-2 element of dp. This is because we cannot rob i-1
                                                      # house. Hence, we can rob ith house and i-2 house
    return dp[-1]
# this is a bottom up approach where we are storing the max amount of money we can rob till ith house in dp array

nums = [2,1,1,2]
print(rob(nums)) # 4

#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and
# it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
# can rob tonight without alerting the police.