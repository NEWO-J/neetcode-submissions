class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1 

        while l < r:
            mid = (l + r) // 2
            print(nums[l], nums[mid], nums[r])
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
            mid = (l + r) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

        print("returning 0")
        return nums[0]
        
        
