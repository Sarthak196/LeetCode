def coin_change(target, coins):
    """
    Function to calculate the minimum number of coins required
    to reach a given target amount using available denominations.

    Parameters:
    - target: int, the total amount for which change is required
    - coins: list of int, available coin denominations

    Returns:
    - int: Minimum number of coins required to make the target amount,
           or -1 if it is not possible to make the amount.
    """
    # Base case: If target is 0, no coins are needed
    if target == 0:
        return 0

    # Initialize a DP array to store minimum coins required for each amount
    # Fill it with a large number (infinity-like value) to indicate that amount is initially unreachable
    dp = [float("inf")] * (target + 1)

    # Minimum coins needed to make amount 0 is 0 (no coins)
    dp[0] = 0

    # Loop through each coin and build solutions
    for coin in coins:
        for amount in range(coin, target + 1):
            # Update the DP value for this amount by checking if using this coin is better than previous value
            # dp[amount - coin] represents the minimum number of coins needed to make the amount amount - coin.
            # Adding 1 accounts for using the current coin to make up the remaining amount.
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If target cannot be achieved, dp[target] will still have float("inf") value
    return dp[target] if dp[target] != float("inf") else -1


coins = [1, 2, 5]
target = 11
result = coin_change(target, coins)
print(result)  # Output: 3 (5 + 5 + 1 = 11)
