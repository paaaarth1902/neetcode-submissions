class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        # index = ord(ch.lower()) - ord('a')
        for string in strs:
            temp = [0] * 26
            for c in string:
                idx = ord(c.lower()) - ord('a')
                temp[idx] += 1
            hashMap[tuple(temp)].append(string)
        
        return list(hashMap.values())
        


        


                


        