class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
            
        l = 0 
        r = len(nums) - 1


        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid 
            else:
                if nums[l] <= target <= nums[mid]:
                    r = mid 
                else:
                    l = mid + 1

        if nums[l] == target:
            return l 
        else:
            return -1
        