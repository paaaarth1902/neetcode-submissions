import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

## Better approach - using priority queue (min - heap)
# T.C : O(n)
        if len(nums) == 0:
            return []
        
        freqMap = {}
        heap = []

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        #Heapify 
        for key, value in freqMap.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                heapq.heappushpop(heap, (value, key))

        
        return [h[1] for h in heap]
        

        



        



        return heap
        