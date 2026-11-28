class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newArr = [[] for i in range(len(nums) + 1)]
        freqMap = {}
        res = []

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        for key, val in freqMap.items():
            newArr[val].append(key)
        
        for i in range(len(newArr) - 1, 0, -1):
            for j in newArr[i]:
                res.append(j)
                if len(res) == k:
                    return res
                
        


        