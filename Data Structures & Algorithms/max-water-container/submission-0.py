class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestvalue = 0
        l = 0
        r = len(heights) - 1
        while r > l:
            # We can eliminate the heights shorter than our current one
            if heights[l] > heights[r]:
                if ((r - l) * heights[r]) > bestvalue:
                    bestvalue = ((r - l) * heights[r])
                r -= 1
            else:
                if ((r - l) * heights[l]) > bestvalue:
                    bestvalue = ((r - l) * heights[l])
                l += 1


        return bestvalue

            # If the current number has no 

        #  Take index into account during calculation
        # Area = r - l * shortest_height
