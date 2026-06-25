class Solution:
    def search_Insert(self, arr, t):
        l = 0
        h = len(arr) - 1

        while l<= h:
            m = l + (h - l) // 2

            if arr[m] == t:
                return m
            elif arr[m] > t:
                h = m - 1
            else:
                l = m + 1

        return l

    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary search approach
        res = []
        res.append(nums[0])

        for i in range(1, len(nums)):
            pos = self.search_Insert(res, nums[i])
            if pos == len(res):
                res.append(nums[i])
            else:
                res[pos] = nums[i]

        return len(res)

        