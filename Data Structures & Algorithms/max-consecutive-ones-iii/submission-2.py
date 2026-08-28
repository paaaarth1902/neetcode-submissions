# O(N) - Optimal solution
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # [1,1,1,0,0,0,1,1,1,1,0]
        l, r, maxLen, zeroes = 0, 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[l] == 0: zeroes -= 1
                l += 1
            
            if zeroes <= k:
                maxLen = max(maxLen, (r - l + 1))

        return maxLen

                


