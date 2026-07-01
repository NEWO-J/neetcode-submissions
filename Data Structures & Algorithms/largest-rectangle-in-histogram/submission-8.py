class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hstack = []
        largestrec = 0
        start = 0
        heights.append(0)

        for i,h in enumerate(heights):  
            start = i
            while hstack and hstack[-1][1] > h:
                farleft, height_popped = hstack.pop()
                largestrec = max(largestrec, height_popped * (i - farleft))
                start = farleft
            hstack.append([start, h])
        
        return largestrec
        