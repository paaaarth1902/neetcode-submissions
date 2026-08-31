# Better than BF approach
# 1. Start with two pointers, l and r to maintain boundary of window
# 2. Along with that, one hashmap that will contain element and its frequency and a maxLen var
# 3. This is effectively: Maximum SubArray with at most 2 unique elements
# 4. Start l and r at 0. Progress with r
# 5. Add rth element in the hashmap and update count of that ele
# 6. Check if size of hashmap is greater than 2.
# 7. if size is greater than 2, we start trimming from left and keep trimming untill the arr[left] has count less than 2 and as soon as count of any ele become 0, remove it
# 8. If size is less than equal to 2, we compute maxlen and return it at end

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r, maxLen = 0, 0, 0
        numMap = {}
        for r in range(len(fruits)):
            numMap[fruits[r]] = numMap.get(fruits[r], 0) + 1

            if len(numMap) > 2:
                while len(numMap) > 2:
                    numMap[fruits[l]] -= 1
                    if numMap[fruits[l]] == 0:
                        del numMap[fruits[l]]
                    l += 1
            
            if len(numMap) <= 2:
                maxLen = max(maxLen, (r - l + 1))
        
        return maxLen