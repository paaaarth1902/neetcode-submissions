class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxLen = 0
        hm = {}

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            
            if len(hm) > k:
                while len(hm) > k:
                    hm[s[l]] -= 1
                    if hm[s[l]] == 0: del hm[s[l]]
                    l += 1
            if len(hm) <= k:
                maxLen = max(maxLen, r - l + 1)
        
        return maxLen