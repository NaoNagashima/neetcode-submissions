class Solution:
    def solve(self, board: List[List[str]]) -> None:        
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def dfs(row, col, change):
            board[row][col] = change

            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]) or board[nr][nc] != "O":
                    continue
                
                dfs(nr, nc, change)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1):
                    dfs(i, j, "T")

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    dfs(i, j, "X")
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"

                

