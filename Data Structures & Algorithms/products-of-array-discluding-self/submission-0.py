class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum approach
        # nums = [1,2,4,6]
        # [1,1,2,8]
        # [48,24,6,1]
        # [48, 24, 12, 8]


        prefixSum = [1] * len(nums)
        suffixSum = [1] * len(nums)

        for i in range(len(nums)):
            if i != 0:
                prefixSum[i] = prefixSum[i - 1] * nums[i - 1]
            else:
                prefixSum[i] = 1

        suffixSum[(len(nums) - 1)] = 1
        for i in range(len(nums)-2, -1, -1):
            suffixSum[i] = suffixSum[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            prefixSum[i] *= suffixSum[i]

        return prefixSum



        