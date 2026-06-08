class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # At each day we aks one simple question - Was there a better day to buy the stock before than today?
        # Best day to buy - at min price; Best day to sell - at max price in future 
        # We make an assumption that at min price, we've bought stock. 
        # So if lower price is encountered - we select that as minPrice
        # we keep evaluating by currPrice - minPrice
        # and update maxProfit on fly
        maxProfit = 0
        minPriceSoFar = float("inf")

        for price in prices:
            if price < minPriceSoFar:
                minPriceSoFar = price
            
            currProfit = price - minPriceSoFar
            maxProfit = max(maxProfit, currProfit)

        return int(maxProfit)

        


        