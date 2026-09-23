class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums = sorted(nums)
        built = []
        seen = {}
        def subs(built, index):
                nonlocal nums
                nonlocal result
                if index == len(nums):
                    if tuple(built) not in seen:
                        result.append(built[:])
                        seen[tuple(built[:])] = True
                    return
                
                built.append(nums[index])
                subs(built, index+1)
                built.pop()

                subs(built, index + 1)

        
        subs(built, 0)
        return result