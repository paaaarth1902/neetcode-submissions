class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = 0

        while low <= high:
            mid = low + (high - low) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            
            if time > h:
                low = mid + 1
            else:
                res = mid
                high = mid -1

        return res


            




