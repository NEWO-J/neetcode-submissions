class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        hstack = collections.deque()
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 0:
                    hstack.append((row,column))
           
        while hstack:
            removed = hstack.popleft()
            r = removed[0]
            c = removed[1]
            if r + 1 < len(grid):
                if grid[r + 1][c] == 2147483647:
                    grid[r + 1][c] = grid[r][c] + 1
                    hstack.append((r+1,c))
            if r- 1 >= 0:
                if grid[r - 1][c] == 2147483647:
                        grid[r - 1][c] = grid[r][c] + 1
                        hstack.append((r-1,c))
            if c + 1 < len(grid[removed[0]]):
                if grid[r][c + 1] == 2147483647:
                    grid[r][c + 1] = grid[r][c] + 1
                    hstack.append((r,c+1))
            if c - 1 >= 0:
                if grid[r][c - 1] == 2147483647:
                    grid[r][c - 1] = grid[r][c] + 1
                    hstack.append((r,c-1))
