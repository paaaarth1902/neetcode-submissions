class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currBest = nums[0]

        for val in nums[1:]:
            currBest = max(currBest + val, val)
            maxSum = max(maxSum, currBest)

        # print(maxSum)
        return maxSum
        