class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # [1,5,4,4,2,3]
        # 5 to 19
        low = max(weights)
        high = sum(weights)
        res = 0

        while low <= high:
            mid = low + (high - low) // 2
            w, daysReq = 0, 0
            for weight in weights:
                w += weight
                if w > mid:
                    daysReq += 1
                    w = weight # start new day with last scrapped weight
            daysReq += 1

            if daysReq <= days:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res


                    
                    
        