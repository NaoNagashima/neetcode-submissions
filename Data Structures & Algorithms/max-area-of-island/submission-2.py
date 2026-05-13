class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def bfs(row, col):
            queue = deque()
            grid[row][col] = 0
            queue.append((row, col))
            result = 1
            
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    queue.append((nr, nc))
                    result += 1
            return result

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = max(area, bfs(i, j))
        
        return area