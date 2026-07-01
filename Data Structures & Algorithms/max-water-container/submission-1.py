class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        mostwater = 0
        r = len(heights) - 1
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            if water > mostwater:
                mostwater = water

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        
        return mostwater
            