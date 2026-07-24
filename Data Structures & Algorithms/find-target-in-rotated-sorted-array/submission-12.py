class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1

        while l < r:
            midpoint = (l + r) // 2
            if nums[r] < nums[midpoint]:
                if nums[l] <= target < nums[midpoint]:
                    r = midpoint - 1
                elif nums[midpoint] == target:
                    return midpoint
                else:
                    l = midpoint + 1
            else:
                if nums[midpoint] < target <= nums[r]:
                    l = midpoint + 1
                elif nums[midpoint] == target:
                    return midpoint
                else:
                    r = midpoint - 1
                


    
        if nums[r] == target:
            return r
        else:
            return -1
