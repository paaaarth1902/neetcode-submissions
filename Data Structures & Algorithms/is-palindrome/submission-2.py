import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "RacecaR"
        # if not s:
        #     return False

        clean_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        p1 = 0
        p2 = len(clean_s) - 1

        while p1 < p2:
            if clean_s[p1] != clean_s[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True
            

        