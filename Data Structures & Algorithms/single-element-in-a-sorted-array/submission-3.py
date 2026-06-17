class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        if len(nums) == 1: return nums[0]
        if len(nums) >= 2 and  nums[1] != nums[0]: return nums[0]

        while low <= high:
            mid = low + (high - low) // 2

            if mid > 0 and mid < len(nums) - 1 and nums[mid] != nums[mid - 1] and nums[mid + 1] != nums[mid]:
                return nums[mid]
            elif mid < len(nums) - 1 and mid % 2 == 0 and nums[mid + 1] != nums[mid]:
                high = mid - 1
            elif mid < len(nums) - 1 and mid % 2 != 0 and nums[mid + 1] != nums[mid]:
                low = mid + 1
            elif mid < len(nums) - 1 and mid % 2 == 0 and nums[mid + 1] == nums[mid]:
                low = mid + 1
            elif mid < len(nums) - 1 and mid % 2 != 0 and nums[mid + 1] == nums[mid]:
                high = mid - 1
            else:
                return nums[high]

            
        