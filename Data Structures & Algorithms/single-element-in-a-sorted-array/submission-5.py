class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        
        while l < h:
            m = l + (h - l) // 2
            
            if m % 2 == 0:
                if m < len(nums) - 1 and nums[m + 1] != nums[m]:
                    h = m
                else:
                    l = m + 1
            elif m > 0 and m < len(nums) - 1 and nums[m] != nums[m + 1] and nums[m] != nums[m - 1]:
                return nums[m]
            else:
                if m < len(nums) - 1 and nums[m + 1] != nums[m]:
                    l = m + 1
                else:
                    h = m

        return nums[l]