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
                    print("White")
                    print(f"Increasing operations to {operations + 1}")
                    operations += 1
                else:
                    print("Black")
                print("R-L = ", r - l + 1)
            if (r - l) + 1 == k:
                print(r - l + 1, k)
                if operations < min_operations:
                    print(f"{operations} Smaller than {min_operations}")
                    min_operations = operations
                    print("Min operations:", min_operations)
                if blocks[l] == 'W':
                    operations -= 1
                l += 1
                


        return min_operations
            
