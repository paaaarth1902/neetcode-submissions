class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPriceSoFar = float("inf")
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minPriceSoFar:
                minPriceSoFar = prices[i]

            currProfit = prices[i] - minPriceSoFar
            maxProfit = max(currProfit, maxProfit)
        
        return int(maxProfit)

            



        