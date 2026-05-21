class Solution {

    public boolean[][] seen;

    public int islandPerimeter(int[][] grid) {
        seen = new boolean[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 1){
                    return perimeter(i, j, grid);
                }
            }
        }
        return -1;
    }

    public int perimeter(int row, int col, int[][] grid){
        if (row < 0 || col < 0 || row >= grid.length || col >= grid[0].length){
            return 1;
        }
        if (grid[row][col] == 0){
            return 1;
        }
        if (seen[row][col]){
            return 0;
        }

        int result = 0;
        seen[row][col] = true;
        result += perimeter(row+1, col, grid);
        result += perimeter(row, col+1, grid);
        result += perimeter(row-1, col, grid);
        result += perimeter(row, col-1, grid);
        
        return result;
    }
}