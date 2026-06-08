

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

## Naive approach would be to populate frequency map - sort thte map absed on frequecy and return first k keys.
## T.C: O(nlogn)

        freqMap = {}
        res =[]

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        sorted_freqMap = {k: v for k, v in sorted(freqMap.items(), key=lambda item: item[1], reverse=True)}

        

        keys_list = list(sorted_freqMap)

        

        for i in range(0, k):
            res.append(keys_list[i])
        
        return res





## Better approach would be usage of min - heap

        
        
