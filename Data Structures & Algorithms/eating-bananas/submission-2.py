class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles_sorted = sorted(piles)

        l = 1
        max = piles_sorted[-1]
        r = max
        min_eat_speed = 0
        min_hours = h
        hours_taken = 0
        while l <= r:
            eat_speed = (l + r) // 2
            print(eat_speed)
            for i in piles_sorted:
                hours_taken += -(-i // eat_speed)
                if hours_taken > h:
                    l = eat_speed + 1
                    break
            
            if hours_taken < h or hours_taken == h:
                min_eat_speed = min(min_eat_speed, eat_speed)
                if hours_taken <= min_hours:
                    min_eat_speed = eat_speed
                    
                r = eat_speed - 1
            hours_taken = 0

        return min_eat_speed