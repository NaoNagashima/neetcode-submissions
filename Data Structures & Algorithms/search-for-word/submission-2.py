class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def bfs(row, col, index):
            if index == len(word):
                return True
            res = False
            if col - 1 >= 0 and board[row][col-1] == word[index] and (row, col-1) not in seen:
                seen.add((row,col-1))
                if bfs(row, col-1, index+1) or res:
                    res = True
                seen.remove((row,col-1))
            if row - 1 >= 0 and board[row-1][col] == word[index] and (row-1, col) not in seen:
                seen.add((row-1, col))
                if bfs(row-1, col, index+1) or res:
                    res = True
                seen.remove((row-1, col))
            if col + 1 < len(board[0]) and board[row][col+1] == word[index] and (row, col+1) not in seen:
                seen.add((row,col+1))
                if bfs(row, col+1, index+1) or res:
                    res = True
                seen.remove((row, col+1))
            if row + 1 < len(board) and board[row+1][col] == word[index] and (row+1, col) not in seen:
                seen.add((row+1, col))
                if bfs(row+1, col, index+1) or res:
                    res = True
                seen.remove((row+1, col))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    seen.add((r,c))
                    if bfs(r,c,1):
                        return True
                    seen.remove((r,c))
        return False
        
