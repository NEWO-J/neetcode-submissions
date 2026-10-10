class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fstack = collections.deque([])

        freshcount = 0
        time = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 2:
                    fstack.append((row,column))
                if grid[row][column] == 1:
                    freshcount += 1
        if freshcount == 0:
            return 0            
        while fstack:
            time += 1
            for _ in range(len(fstack)):
                removed = fstack.popleft()
                r = removed[0]
                c = removed[1]
                if r + 1 < len(grid):
                    if grid[r+1][c] == 1:
                        grid[r+1][c] = 2
                        freshcount -= 1
                        fstack.append((r+1,c))

                if r - 1 >= 0:
                    if grid[r-1][c] == 1:
                        grid[r-1][c] = 2
                        freshcount -= 1
                        fstack.append((r-1, c))
                
                if c + 1 < len(grid[r]):
                    if grid[r][c+1] == 1:
                        grid[r][c+1] = 2
                        freshcount -= 1
                        fstack.append((r, c+1))
                
                if c - 1 >= 0:
                    if grid[r][c-1] == 1:
                        grid[r][c-1] = 2
                        freshcount -= 1
                        fstack.append((r, c-1))

        if freshcount > 0:
            return -1
        else:
            return time - 1