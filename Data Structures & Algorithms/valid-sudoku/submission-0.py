class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

#       Validating rows
        for i in range(9):
            s = set()
            for j in range(9):
                element = board[i][j]
                if element in s:
                    return False
                elif element != ".":
                    s.add(element)
                else:
                    continue

#       Validating columns
        for i in range(9):
            s = set()
            for j in range(9):
                element = board[j][i]
                if element in s:
                    return False
                elif element != ".":
                    s.add(element)
                else:
                    continue


        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                seen = set()

                for r in range(row, row + 3):
                    for c in range(col, col + 3):

                        val = board[r][c]

                        if val == ".":
                            continue

                        if val in seen:
                            return False

                        seen.add(val)

        return True

        
        