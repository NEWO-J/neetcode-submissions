class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        exists = False
        seen = {}
        def dfs(r, c, index):
            nonlocal exists
            nonlocal seen
            if index == len(word):
                exists = True
                return 
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]):
                return
            if board[r][c] != word[index] or (r,c) in seen:
                return
            
            seen[(r,c)] = True
            
            dfs(r + 1, c, index + 1)
            dfs(r - 1, c, index + 1)
            dfs(r, c + 1, index + 1)
            dfs(r, c - 1, index + 1) 

            del seen[(r,c)]


        for row in range(len(board)):
            for column in range(len(board[row])):
                    dfs(row, column, 0)

        return exists
