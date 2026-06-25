# nums = [4,5,6,7,0,1,2]
class Solution:
    def find_lowest_val(self, nums):
        l = 0
        h = len(nums) - 1

        while l < h:
            m = l + (h - l) // 2

            if nums[h] < nums[m]:
                l = m + 1
            else:
                h = m
        return l

    def bs(self, nums,l, h, t):
        while l <= h:
            m = l + (h - l) // 2

            if nums[m] == t:
                return m
            elif nums[m] > t:
                h = m - 1
            else:
                l = m + 1

        return - 1


    def search(self, nums: List[int], target: int) -> int:

        l = self.find_lowest_val(nums)

        h1 = self.bs(nums, 0, l - 1, target)
        h2 = self.bs(nums, l, len(nums) - 1, target)

        if h1 != -1:
            return h1
        else:
            return h2