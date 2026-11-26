class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in numMap:
                numMap[nums[i]] = i
            else:
                return [numMap[complement], i]



        