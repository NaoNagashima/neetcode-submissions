class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        blocks = {}

        for i in range(9):
            rows[i] = []
            cols[i] = []
            blocks[i] = []

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    block = 3 *(row//3) + (col//3)
                    val = board[row][col]
                    if val in rows[row]:
                        return False
                    elif val in cols[col]:
                        return False
                    elif val in blocks[block]:
                        return False
                    else:
                        rows[row].append(val)
                        cols[col].append(val)
                        blocks[block].append(val)
        return True