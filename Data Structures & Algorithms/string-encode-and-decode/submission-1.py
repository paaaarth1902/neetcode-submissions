class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += (str(l) + "#" + s)
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            s1 = s[j + 1: j + 1 + l]
            res.append(s1)
            i = j + 1 + l

        return res

                
