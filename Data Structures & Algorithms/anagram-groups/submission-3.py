from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for c in strs:
            arr = [0] * 26

            for i in c:
                arr[ord(i) - ord('a')] += 1
            
            ans[tuple(arr)].append(c)
        
        return list(ans.values())