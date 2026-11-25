class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        maxLen = 0

        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            if s[r] not in seen:
                seen.add(s[r])
                maxLen = max(maxLen, (r - l + 1))
        
        return maxLen

        