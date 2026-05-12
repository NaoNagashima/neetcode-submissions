class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        def bfs(row, col) -> bool:
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            if grid[row][col] != "1":
                return False
            grid[row][col] = "0"
            bfs(row-1, col)
            bfs(row, col-1)
            bfs(row+1, col)
            bfs(row, col+1)
            return True
    

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if bfs(i,j):
                    result += 1
        return result
                
    