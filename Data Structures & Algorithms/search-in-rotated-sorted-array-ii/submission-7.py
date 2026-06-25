class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if duplicates are present, different logic comes in play

        l = 0 
        h = len(nums) - 1

        while l <= h:
            m = l + (h - l) //2

            if nums[m] == target:
                return True
            
            elif nums[l] == nums[m] == nums[h]:
                l += 1
                h -= 1

            elif nums[m] >= nums[l]:
                if nums[l] <= target and target <= nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target and target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1

        return False
        