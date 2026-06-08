class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        pair = []
        firstOcc = -1
        lastOcc = -1

        while low <= high:
            mid = (low + (high - low) // 2)

            if nums[mid] == target:
                firstOcc = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + (high - low) // 2)

            if nums[mid] == target:
                lastOcc = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        pair.append(firstOcc)
        pair.append(lastOcc)

        return pair



        