class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case is length of built array = length of nums
        result = []
        built = []
        seen = {}
        def perm(built, seen):
            if len(built) == len(nums):
                result.append(built[:])
                return
            
            for num in nums:
                if num not in seen:
                    seen[num] = True
                    built.append(num)
                    perm(built, seen)
                    built.pop()
                    seen.pop(num)
                
        perm(built, seen)
        return result
            
            
