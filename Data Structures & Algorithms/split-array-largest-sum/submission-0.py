class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        res = 0

        while low <= high:
            mid = low + (high - low) // 2

            subsetcount = 0
            n = 0
            for num in nums:
                n += num
                if n > mid:
                    subsetcount += 1
                    n = num
            subsetcount += 1

            if subsetcount <= k:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        
        return res

                    
        