class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        curr=0
        currlen=0

        for num in numset:
            if num - 1 not in numset:
                currlen = 1
                curr=num
            
            while curr + 1 in numset:
                currlen+=1
                curr+=1
            
            longest=max(currlen, longest)
        
        return longest
