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
                    print(row, col, board[row][col],block)
                    if val in rows[row]:
                        print(rows)
                        return False
                    elif val in cols[col]:
                        print(cols)
                        return False
                    elif val in blocks[block]:
                        print(blocks)
                        return False
                    else:
                        rows[row].append(val)
                        cols[col].append(val)
                        blocks[block].append(val)
        return True