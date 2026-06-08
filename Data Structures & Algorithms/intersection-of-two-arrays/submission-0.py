class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsSet = set(nums1)

        numsSet &= set(nums2)

        return list(numsSet)