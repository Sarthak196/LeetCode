def coinChange(coins, amount):
    # If the amount is 0, no coins are needed.
    if amount == 0:
        return 0

    # Create a dp array of size amount + 1, initialized with amount + 1.
    # This is because the maximum number of coins needed will not exceed amount + 1.
    dp = [amount + 1] * (amount + 1)

    # Base case: To make amount 0, 0 coins are needed.
    dp[0] = 0

    # Iterate over each coin in the coins list.
    for coin in coins:
        # For each coin, update the dp array for all amounts from coin to amount.
        for i in range(coin, amount + 1):
            # Update dp[i] to the minimum of its current value and dp[i - coin] + 1.
            # dp[i - coin] + 1 represents using one more coin (coin) to make up the amount i.
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still amount + 1, it means it's not possible to make up the amount with the given coins.
    # Otherwise, return dp[amount] which is the minimum number of coins needed.
    return dp[amount] if dp[amount] != amount + 1 else -1

# Test cases
print(coinChange([1, 2, 5], 11)) # 3