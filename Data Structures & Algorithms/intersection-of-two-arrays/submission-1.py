class Solution:

    def binarySearch(self, nums, target):
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m - 1
            else:
                l = m + 1
        
        return -1

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()
        r = []

        for num in set(nums1):
            res = self.binarySearch(nums2, num)
            if res != -1:
                r.append(num)

        return r

        