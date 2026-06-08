class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)

        newArr =[1] * 2 * n
        newArr = nums + nums

        return newArr





        