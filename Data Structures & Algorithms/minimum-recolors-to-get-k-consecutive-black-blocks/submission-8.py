class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        operations = 0
        min_operations = float('inf')
        l = 0
        r = -1
        while r < len(blocks) - 1:
            if (r - l) + 1 != k:
                r += 1
                if blocks[r] == 'W':
                    operations += 1
            if (r - l) + 1 == k:
                if operations < min_operations:
                    min_operations = operations
                if blocks[l] == 'W':
                    operations -= 1
                l += 1
                


        return min_operations
            
