class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedNums = sorted(nums1 + nums2)

        l = 0
        h = len(sortedNums) - 1

        mid = ( l + h ) // 2

        if len(sortedNums) % 2 != 0:
            return sortedNums[mid]
        else:
            return (sortedNums[mid] + sortedNums[mid + 1]) / 2

        
        