class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        threebythree = {}
        columncheck = {}
        rowcheck = {}
        ### Check if the value has already appeared in the row
        ### Check if the value has already appeared in the column
        ### Check if the value has already appeared in the 3x3
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if r < 3:
                    if c < 3:
                        box = 1
                    elif c < 6:
                        box = 2
                    else: 
                        box = 3
                elif r < 6:
                    if c < 3:
                        box = 4
                    elif c < 6:
                        box = 5
                    else:
                        box = 6
                else:
                    if c < 3:
                        box = 7
                    elif c < 6:
                        box = 8
                    else:
                        box = 9
                if value != ".":
                    if str(value) + ":" + str(box) in threebythree:
                        return False
                    else:
                        threebythree[str(value) + ":" + str(box)] = True
                    if str(value) + ":" + str(r) in rowcheck:
                        return False
                    else:
                        rowcheck[str(value) + ":" + str(r)] = True
                    if str(value) + ":" + str(c) in columncheck:
                        return False
                    else:
                        columncheck[str(value) + ":" + str(c)] = True
        return True

           
