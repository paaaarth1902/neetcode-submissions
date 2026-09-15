class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table={}
        if len(s) != len(t): return False

        for c in s:
            if c not in table:
                table[c] = 1
            else:
                table[c] += 1
        
        for c in t:
            if c not in table or table[c] == 0:
                return False
            else:
                table[c] -= 1
        
        return True
        