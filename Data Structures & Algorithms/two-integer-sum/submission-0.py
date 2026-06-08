class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numsMap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement not in numsMap:
                numsMap[num] = i
            else:
                return [numsMap[complement], i]
        