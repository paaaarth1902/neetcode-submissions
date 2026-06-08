class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Intuitive Observational approach (Find prefix product and suffixProduct, max out of these is maxProduct)

        prefixProduct, suffixProduct = 1, 1
        maxProduct = -100000
        for i in range(len(nums)):
            if prefixProduct == 0:
                prefixProduct = 1
            if suffixProduct == 0:
                suffixProduct = 1
            prefixProduct *= nums[i]
            suffixProduct *= nums[len(nums) - i - 1]
            maxProduct = max(maxProduct, max(prefixProduct, suffixProduct))

        return maxProduct

