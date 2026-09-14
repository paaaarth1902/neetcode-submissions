class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                return True
        return False

        