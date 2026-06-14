class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # Two pointer - O(nlogn), O(1)
        sortedNums = sorted(nums)
        low = 0
        high = len(nums) - 1
        sol = -1

        if len(nums) <= 1: return -1

        while low < high:
            sum = sortedNums[low] + sortedNums[high]

            if sum < k:
                sol = max(sum, sol)
                low += 1
            else:
                high -= 1

        return sol


        