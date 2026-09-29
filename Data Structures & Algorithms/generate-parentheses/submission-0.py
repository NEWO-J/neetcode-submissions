class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        openp = []
        closedp = []
        def genPar(built, open_count, closed_count):
            nonlocal result
            if len(built) == 2 * n:
                result.append(built[:])
                return

            if open_count < n:
                genPar(built + "(", open_count + 1, closed_count)
            if closed_count < open_count:
                genPar(built + ")", open_count, closed_count + 1)


        genPar("", 0, 0)
        return result