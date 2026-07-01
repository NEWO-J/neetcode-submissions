class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        Ltallest = 0
        Rtallest = 0
        result = 0
        while l < r:

            if height[l] > Ltallest:
                Ltallest = height[l]
            if height[r] > Rtallest:
                Rtallest = height[r]

            if height[l] < height[r]:
                water = Ltallest - height[l]
                if water <= 0:
                    result += 0
                else:
                    result += water
                l += 1
                
            else:
                water = Rtallest - height[r]
                if water <= 0:
                    result += 0
                else:
                    result += water

                r -= 1
          

        return result