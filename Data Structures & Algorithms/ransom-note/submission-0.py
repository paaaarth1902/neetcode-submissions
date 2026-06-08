class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazineMap = {}

        for c in magazine:
            magazineMap[c] = magazineMap.get(c, 0) + 1


        for c in ransomNote:
            if c not in magazineMap.keys():
                return False
            magazineMap[c] -= 1
            if magazineMap[c] < 0:
                return False

        
        return True
        

        