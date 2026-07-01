class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        water_height = 0
        total_water = 0
        leftmost_height = 0
        rightmost_height = 0

        while i < j:
            leftmost_height = max(leftmost_height, height[i])
            rightmost_height = max(rightmost_height, height[j])
            water_height = min(leftmost_height, rightmost_height)

            if height[i] > height[j]:
                j -= 1   
            else:
                i += 1

            if water_height - height[i] > 0:
                total_water += water_height - height[i]
 
            if water_height - height[j] > 0:
                total_water += water_height - height[j]   


        return total_water