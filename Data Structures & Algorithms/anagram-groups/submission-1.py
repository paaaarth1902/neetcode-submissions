class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupMap = {}

        for val in strs:
            sortedVal = ''.join(sorted(val))
            if sortedVal not in groupMap:
                groupMap[sortedVal] = []
            groupMap[sortedVal].append(val)

        return list(groupMap.values())
                

        