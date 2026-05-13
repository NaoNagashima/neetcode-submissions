class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        direction = [[1,0],[0,1],[-1, 0],[0,-1]]
        
        def bsf(distanceToTreasure, row, col):
            grid[row][col] = distanceToTreasure
            newDistance = distanceToTreasure + 1

            for dr, dc in direction:
                nr, nc = dr + row, dc + col
                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == -1 or grid[nr][nc] <= newDistance:
                    continue
                bsf(newDistance, nr, nc)
            

        # For loop to find every treasure
        for i in range(len(grid)):
            for j in range(len(grid[i])):   
                if grid[i][j] == 0:
                    bsf(0, i, j)