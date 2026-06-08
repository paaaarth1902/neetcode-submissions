class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Time complexity expected is O(log n) meaning some variation ob Binary Search is expected
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + (high - low) // 2)
            # check if left neightbour greater
            if mid > 0 and nums[mid] < nums [mid - 1]:
                high = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                return mid

