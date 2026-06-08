class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # 1 [1,2,3,4]
        # [1,2,3,4] 1
        Leftresult = [1] * len(nums)
        pre_val = 1
        for i in range(len(nums)):
            Leftresult[i] = pre_val
            pre_val *= nums[i]
        
        Rightresult = [1] * len(nums)
        suff_val = 1
        for i in range(len(nums) - 1, -1, -1):
            Rightresult[i] = suff_val
            suff_val *= nums[i]

        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = Leftresult[i] * Rightresult[i]

        return result



        

        