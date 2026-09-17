class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # 1, []
        # [1, 1, 2, 8]
        # [ 48, 24, 6, 6]

        prePro = [1] * len(nums)
        suffPro = [1] * len(nums)
        
        k = 1
        for i in range(len(nums)):
            prePro[i] = k
            k *= nums[i]

        m = 1
        for i in range(len(suffPro) - 1, -1, -1):
            suffPro[i] = m 
            m *= nums[i]

        res = []
        for i in range(len(prePro)):
            res.append(prePro[i] * suffPro[i])
        
        return res

