class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) + 1
        smallest = float('inf')
        while l < r:
            mid = (l + r) // 2
            total = 0
            for i in range(len(piles)):        
                time = -(-piles[i] // mid)
                total += time
            if total <= h:
                r = mid
                smallest = min(smallest, mid)
            if total > h:
                l = mid + 1
                
        
        return smallest