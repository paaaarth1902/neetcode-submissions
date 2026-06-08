class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # core insight - we ask if current element is the start 
        # we check this by checking if val - 1 exists or not
        # if it not exists, we found a start and since we are only interested in length, we start length as 1 
        # now we check if val + 1 is there in the array if it is, we increase length 
        # we keep doing this check till val + 1 is there and increasing length 
        # keep updating the longest in each iteration 

        longest = 0 # storing the longest variable 
        numSet = set(nums) # transferring elemnts in set to get rid of duplicates

        for value in numSet:
            if value-1 not in numSet: # only concerned for start of any sequence
                length = 1
                currValue = value

                while (currValue + 1) in numSet: # keep increasing length till sequence is present 
                    length += 1
                    currValue += 1

                longest = max(length, longest) # keep updating longest 

        
        return longest
        