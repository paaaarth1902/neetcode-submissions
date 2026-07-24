class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we use Binary search with small modification.
        # we check if mid is greater than end. If mid is greater than end, we conclude that the right half is not sorted and left half is sorted.
        # we know minimum element will always be in unsorted half

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low ) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
