class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        # [3, 5, 6, 7]
        cnt = 0
        for i in range(len(nums)):
            l = i
            h = len(nums) - 1
            res = i - 1

            while l <= h:
                m = l + (h - l) // 2

                if nums[m] <= target - nums[i]:
                    res = m
                    l = m + 1
                else:
                    h = m - 1
            if res < i:
                cnt += 0
            else:
                cnt += 2**(res - i)

        return cnt % (10**9 + 7)