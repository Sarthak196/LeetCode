def maxProfit(prices):
    Profit = 0
    for sell in range(1, len(prices)): # sell is the right pointer which starts from 2nd element
        buy = 0 # buy always starts from 0th index as we can buy at any future time of sell
        while buy < sell:
            if prices[buy] < prices[sell]:
                Profit = max(Profit,prices[sell] - prices[buy])
            buy += 1
    return Profit

prices = [10,5,1,5,100]
print(maxProfit(prices)) # 99