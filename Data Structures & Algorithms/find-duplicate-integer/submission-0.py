class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = {}


        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1

        for n in nums:
            if hm[n] > 1:
                return n
            
        