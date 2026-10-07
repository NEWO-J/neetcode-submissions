class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            if r > len(grid) - 1 or c > len(grid[r]) - 1 or r < 0 or c < 0:
                return
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        count = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == "1":
                    count += 1
                    dfs(row, column)
        
        return count