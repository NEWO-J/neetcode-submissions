class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        built = []
        def sub(built, index):
            nonlocal result
            if index == len(nums):
                result.append(built[:])
                return None

            
            # include
            built.append(nums[index])
            sub(built, index + 1)
            built.pop()

            sub(built, index + 1)

        
        sub(built, 0)
        return result

