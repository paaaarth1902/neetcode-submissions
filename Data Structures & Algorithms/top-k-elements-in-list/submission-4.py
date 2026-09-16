class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}

        for num in nums:
            table[num] = table.get(num, 0) + 1
        
        arr = [[] for i in range(len(nums) + 1)]

        for m, v in table.items():
            arr[v].append(m)
        
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for c in arr[i]:
                res.append(c)
                if len(res) == k:
                    return res
        