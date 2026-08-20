class Solution:
    
    def findDuplicate(self, nums: List[int]) -> int:
        s = 0
        f = 0
        f = nums[nums[f]]
        s = nums[s]

        while f != s:
            f = nums[nums[f]]
            s = nums[s]
        
        new = 0 
        while new != f:
            f = nums[f]
            new = nums[new]

        return new

            