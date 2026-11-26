class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charMap = {}

        for c in s:
            charMap[c] = charMap.get(c, 0) + 1

        for m in t:
            if m not in charMap:
                return False
            charMap[m] -= 1
            if charMap[m] == 0:
                charMap.pop(m)
        
        return len(charMap) == 0