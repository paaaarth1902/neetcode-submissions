class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        lowerS = s.lower()
        while l < r:
            while l < r and not lowerS[l].isalnum():
                l+= 1
            while l < r and not lowerS[r].isalnum():
                r-= 1
            if lowerS[l] != lowerS[r]:
                return False
            l += 1
            r -= 1

        return True
        