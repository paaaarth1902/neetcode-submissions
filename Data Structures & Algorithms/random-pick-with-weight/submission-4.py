# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

class Solution:
    # [1, 3, 5] -> [1, 4, 9]
    def __init__(self, w: List[int]):
        # Initialize an empty list
        self.nums = w

        self.prefix_sum = []
        self.prefix_sum.append(self.nums[0])
        for i in range(1, len(self.nums)):
            self.prefix_sum.append(self.nums[i] +self.prefix_sum[i - 1])

        self.n = sum(self.nums)
        

    def pickIndex(self) -> int:
        l = 0
        h = len(self.prefix_sum) - 1
        r = random.randint(1, self.n)

        while l <= h:
            m = l + (h - l) // 2

            if self.prefix_sum[m] >= r:
                h = m - 1
            else:
                l = m + 1

        return l
