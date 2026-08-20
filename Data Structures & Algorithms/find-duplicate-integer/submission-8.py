class Solution:
    
    def findDuplicate(self, nums: List[int]) -> int:
        f = nums[nums[0]]
        s = nums[0]

        while f != s:
            f = nums[nums[f]]
            s = nums[s]
        
        s = 0 
        while s != f:
            f = nums[f]
            s = nums[s]

        return s

            