class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxTotal = 0
        def dfs(r, c):
            if r > len(grid) - 1 or c > len(grid[r]) - 1 or r < 0 or c < 0:
                return 0 
            if grid[r][c] == 0:
                return 0 
            
            grid[r][c] = 0
            
            return(1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    runningTotal = dfs(row, column)
                    maxTotal = max(runningTotal, maxTotal)
        
        return maxTotal
