class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        maxval = max(piles)
        r = maxval
        min_eat_speed = maxval
        hours_taken = 0
        while l <= r:
            eat_speed = (l + r) // 2
            for i in piles:
                hours_taken += -(-i // eat_speed)
                if hours_taken > h:
                    l = eat_speed + 1
                    break
            
            if hours_taken < h or hours_taken == h:
                min_eat_speed = min(min_eat_speed, eat_speed)
                r = eat_speed - 1
            hours_taken = 0

        return min_eat_speed