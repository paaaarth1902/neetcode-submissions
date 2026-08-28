# 1. start with l and r at first char along with empty hashmap and maxLen = 0
# 2. Progress r forward with loop and keep checkinf if s[r] has been seen before and if its value in hashmap belongs in thew indow cuur window charMap[s[r]] >= l
# 3. If yes, move l forward to charMap[s[r]] + 1 
# Update map to have s[r]
#  4. Compute maxlen

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxLen = 0, 0, 0
        charMap = {}

        for r in range(len(s)):
            if s[r] in charMap and charMap[s[r]] >= l:
                l = charMap[s[r]] + 1
            charMap[s[r]] = r
            
            maxLen = max(maxLen, (r - l + 1))

        return maxLen
        