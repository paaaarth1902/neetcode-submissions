class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in numMap:
                return [numMap[complement], i]
            numMap[n] = i
        return []
