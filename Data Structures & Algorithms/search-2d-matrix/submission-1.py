class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        l = 0
        h = (r * c) - 1

        while l <= h:
            m = l + (h - l) // 2

            if matrix[m // c][m % c] == target:
                return True
            elif matrix[m // c][m % c] > target:
                h = m - 1
            else:
                l = m + 1
        
        return False
        