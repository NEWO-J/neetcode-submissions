class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

            result = []
            built = []
            def sub(built, index):
                nonlocal nums
                nonlocal result
                if index == len(nums):
                    result.append(built[:])
                    return
            
                sub(built, index + 1)
                

                built.append(nums[index])
                sub(built, index + 1)
                built.pop()
            

            sub(built, 0)
            return result
    