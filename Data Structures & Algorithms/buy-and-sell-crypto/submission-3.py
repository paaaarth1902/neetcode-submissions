class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        profit = 0

        best = float("inf")

        for i in range(len(prices)):
            if prices[i] < best:
                best = prices[i]
            else:
                profit = prices[i] - best
                maxProfit = max(profit, maxProfit)
        
        return maxProfit
