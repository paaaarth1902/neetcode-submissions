class Solution:
    # d = sum
    def subsetCountChecker(self, nums, d, k):
        subsets, s = 0, 0
        for n in nums:
            s += n
            if s > d:
                subsets += 1
                s = n
        subsets += 1

        return subsets <= k


    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)
        res = 0

        while l <= h:
            m = l + (h - l) // 2

            if self.subsetCountChecker(nums, m, k):
                res = m
                h = m - 1
            else:
                l = m + 1
        
        return res


        