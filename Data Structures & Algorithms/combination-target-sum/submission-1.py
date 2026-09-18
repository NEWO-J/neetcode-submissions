class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        built = []
        def combo(built, total, index):
            nonlocal result
            nonlocal target
            nonlocal nums
            if total >= target or index > len(nums) - 1:
                if total == target:
                    result.append(built[:])
                return
            
            # include same index
            built.append(nums[index])
            combo(built, total + nums[index], index)
            removed = built.pop()
            total -= removed
            combo(built, total + nums[index], index + 1)

            return

        
        combo(built, 0, 0)
        return result