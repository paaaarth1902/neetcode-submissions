class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointer approach
        # We initialise 2 pointers with i at start and j at len(heights) - 1
        # we compute (j - 1) * min(heights[i], heights[j]) - as we are only concerned with shorter height between 2 bars for area computation
        # Keep updating maxWater on fly by computing max(maxWater, currArea)
        # We will always be limited by shorted wall / heights[i]. So goal is to maximise the shortest wall, meaning we will always move the shorter wall's pointer
        # Doing this we can encorporate greedy approach


        maxWater = 0
        p1 = 0
        p2 = len(heights) - 1

        while (p2 > p1):
            currArea = (p2 - p1) * min(heights[p1], heights[p2])
            maxWater = max(maxWater, currArea)

            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1
        
        return maxWater