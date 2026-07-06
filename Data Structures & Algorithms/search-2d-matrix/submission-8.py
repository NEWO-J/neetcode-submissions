class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)

        l = 0
        r = n - 1
        index = 0
        midpoint = r - l // 2
        
        while r - l >= 1:
            midpoint = (r + l) // 2
            if matrix[midpoint][0] > target:
                r = midpoint - 1
            elif matrix[midpoint][0] < target:
                l = midpoint + 1
            else:
                return True
        
        if matrix[l][0] > target:
            index = l - 1
        else:
            index = l
            
        l = 0 
        r = len(matrix[index])
        
        if matrix[index][l] == target:
            return True
        if r == 1:
            return False

        while r - l >= 1:
            midpoint = (r + l) // 2
            if matrix[index][midpoint] > target:
                r = midpoint - 1
            elif matrix[index][midpoint] < target:
                l = midpoint + 1
            else:
                return True
        
        if matrix[index][l:r+1]:
            return matrix[index][l] == target

        return False
        
       

    


            

