class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        while r - l > 1:

            midpoint = (l + r) // 2

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                l = midpoint  
            else:
                r = midpoint

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        
        return - 1

        