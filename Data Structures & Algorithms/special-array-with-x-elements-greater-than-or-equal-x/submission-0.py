class Solution:
    def specialArray(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)

        while (low <= high):
            mid = low + (high - low) // 2
            cnt = 0

            for i in range(len(nums)):
                if nums[i] >= mid:
                    cnt+=1
            
            if cnt == mid:
                return cnt
            elif cnt < mid:
                high = mid - 1
            else:
                low = mid + 1

        return -1

        