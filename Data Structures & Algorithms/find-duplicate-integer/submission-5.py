class Solution:
    
    def findDuplicate(self, nums: List[int]) -> int:
        f = nums[nums[0]]
        s = nums[0]

        while f != s:
            f = nums[nums[f]]
            s = nums[s]
        
        new = 0 
        while new != f:
            f = nums[f]
            new = nums[new]

        return new

            