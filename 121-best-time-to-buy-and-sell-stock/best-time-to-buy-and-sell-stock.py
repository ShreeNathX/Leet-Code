class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit, bestbuy = 0, prices[0]

        for i in range(len(prices)):
            if prices[i] > bestbuy:
                max_profit = max(max_profit, prices[i] - bestbuy)
            else:
                bestbuy = min(bestbuy, prices[i])
        
        return max_profit