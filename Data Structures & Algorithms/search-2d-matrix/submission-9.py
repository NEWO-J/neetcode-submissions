class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix[0])
        
        l = 0
        r = len(matrix) * length
        re
        while l < r:
            midpoint = (l + r) // 2
            m_1 = midpoint // length 
            m_2 = midpoint % length
            l_1 = l // length
            l_2 = l % length
            r_1 = r // length
            r_2 = r % length
            
            if matrix[m_1][m_2] > target:
                r = midpoint
            elif matrix[m_1][m_2] < target:
                l = midpoint + 1
            else:
                return True

        
        return False
    


            

