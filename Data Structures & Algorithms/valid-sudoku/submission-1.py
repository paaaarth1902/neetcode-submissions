class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    row_key = f"{val} in row {i}"
                    col_key = f"{val} in col {j}"
                    box_key = f"{val} in box {i // 3}-{j // 3}"

                    if row_key in hashset or col_key in hashset or box_key in hashset:
                        return False
                    
                    hashset.add(row_key)
                    hashset.add(col_key)
                    hashset.add(box_key)
        return True
