class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        col = len(matrix[0])
        total = rows * col

        start = 0
        end = total - 1

        while (end >= start):
            # m = start + (end - start) / 2
            m = int(( start + end ) / 2)
            i = (m // col)
            j = (m % col)
            val = matrix[i][j]

            if target == val:
                return True
            elif target > val:
                start = m + 1
            else:
                end = m - 1

        return False
        