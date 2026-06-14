class Solution:
    def mySqrt(self, x: int) -> int:
        # 13 - [1,2,3,4,5,6,7,8,9,10,11,12,13]
        low = 0
        high = x - 1
        res = 0

        if x<= 1:
            return x

        while low <= high:
            mid = low + (high - low) // 2

            if mid**2 > x:
                high = mid - 1
            else:
                res = mid
                low = mid + 1
        
        return res

        