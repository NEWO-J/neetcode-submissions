class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # biggest possible eating speed in max value
        # smallest possible eating speed is 1.

        maxval = piles[0]

        for pile in piles:
            maxval = max(maxval, pile)

        i = 1
        j = maxval
        hours_taken = 0

        while i < j:
            eat_speed = (i + j) // 2
            print(eat_speed)
            for pile in piles:
                hours_taken +=  -(pile // -eat_speed) 
            
            if hours_taken <= h:
                j = eat_speed
            else:
                i = eat_speed + 1
            hours_taken = 0

        return i
 
