class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        idealSum = n * (n + 1) // 2
        sum1 = 0
        for val in nums:
            sum1+= val
        return idealSum - sum1
