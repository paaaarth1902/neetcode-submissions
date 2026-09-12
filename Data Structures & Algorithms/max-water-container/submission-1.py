class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol, maxVol = 0, 0
        i, j = 0, len(heights) - 1

        while i < j:
            vol = (j - i) * min(heights[i], heights[j])
            maxVol = max(vol, maxVol)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return maxVol
        