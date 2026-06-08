class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return []

        anagramMap = {}

        for string in strs:
            key = ''.join(sorted(string))
            if key not in anagramMap:
                anagramMap[key] = []
            anagramMap[key].append(string)

        return list(anagramMap.values())

