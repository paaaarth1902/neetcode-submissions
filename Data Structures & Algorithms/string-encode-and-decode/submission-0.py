class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStrList = []
        for stringToCheck in strs:
            encodedStrList.append(str(len(stringToCheck)) + "#" + stringToCheck)
        
        return "".join(encodedStrList)
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while (i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            
            length = int(s[i:j])

            i = j + 1

            result.append(s[i : i + length])

            i = i + length
            
        return result



        

       
