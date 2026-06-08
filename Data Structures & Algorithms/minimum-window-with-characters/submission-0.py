class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charMap ={}

        for c in t:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1

        left = 0
        mapEleCount = len(charMap)
        have = 0
        result =""
        minLen = float("inf")
        for right in range(len(s)):
            if s[right] in charMap:
                charMap[s[right]] -= 1
                if charMap[s[right]] == 0:
                    have += 1

            
            while have == mapEleCount:
                if (right - left + 1) < minLen:
                    minLen = (right - left + 1)
                    result = s[left:right + 1]
                if s[left] in charMap:
                    charMap[s[left]] += 1
                    if charMap[s[left]] == 1:
                        have -= 1
                left += 1
        
        return result






        
        