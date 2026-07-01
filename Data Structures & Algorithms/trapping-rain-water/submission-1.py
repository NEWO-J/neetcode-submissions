class Solution:
    def trap(self, height: List[int]) -> int:
        glh = 0
        grh = 0
        waterline = 0
        l = 0
        r = len(height) - 1
        total = 0

        while l < r:
            if height[l] > glh:
                glh = height[l]
            if height[r] > grh:
                grh = height[r]
            
            if height[l] >= grh:
                waterline = grh
            if height[r] >= glh:
                waterline = glh

            if height[l] < waterline:
                total += waterline - height[l]
            if height[r] < waterline:
                total += waterline - height[r]
            
            if grh > glh:
                l += 1
            else:
                r -= 1

        return total
 

