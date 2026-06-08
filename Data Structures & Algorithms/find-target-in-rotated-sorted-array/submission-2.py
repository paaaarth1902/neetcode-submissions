class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: Find idx of minimum element (number of times this array has been sorted)
        # For this we will compare mid element with nums[high] to check if right half is sorted or not

        low = 0
        high = len(nums) - 1

        while (low < high):
            mid = (low + (high - low) // 2)

            if nums[mid] >= nums[high]:
                low = mid + 1
            else:
                high = mid

        # Minimum element will be at idx = low
        # Step 2: We now have two sorted subarrays inside this one rotated sorted array
        # First: start -> low - 1 and Second: mid -> len(nums) - 1
        # We apply two Binary Search now and the one that return non -1 value will return the idx of that element as it can be present inside one of these subarrays

        def binarySearch(arr: List[int], start: int, end: int) -> int:

            while(start <= end):
                mid = (start + (end - start) // 2)

                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1

            return -1


        res1 = binarySearch(nums, 0, low - 1)
        res2 = binarySearch(nums, low, len(nums) - 1)

        if res1 != -1:
            return res1
        elif res2 != -1:
            return res2
        else:
            return -1


        