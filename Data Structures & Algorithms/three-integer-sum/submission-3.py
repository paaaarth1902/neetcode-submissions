class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1, 0, 1, 2, -1, -4]
        # sorted array = [-4, -1, -1, 0, 1, 2]
        # res = []

        # condition states that nums[i] + nums[j] + nums[k] == 0 should be true
        # This can be solved as modified version of Two Sum.
        # condition can be modified as -> nums[j] + nums[k] = -nums[i]
        # T.C cannot exceed O(n^2) - meaning at most two loops
        # We start with one outer loop that runs from i = 0 to len(nums) - 1
        # And a inner loop with j = i + 1 and k = len(nums) - 1
        # Inside this inner loop - we start to check summation of nums[j] + nums[k]
        # Considering we can sort the array, we initialise j and k to i + 1 and len(nums) - 1
        # Compute sum = nums[j] + nums[k]
        # if sum > -nums[i], j+= 1; if sum < -nums[i], k -= 1; else append trio i,j,k to res
        # move the elements from res to set

        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while (k > j):
                sum = nums[j] + nums[k]
                if sum < nums[i] * -1:
                    j += 1
                elif sum > nums[i] * -1:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while (j < k and nums[j] == nums[j-1]):
                        j += 1
                    

        return res
        