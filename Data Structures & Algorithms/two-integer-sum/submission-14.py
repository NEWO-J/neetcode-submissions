class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums) - 1):
            diff = target - nums[i]
            if diff in hashmap and i != hashmap[diff]:
                return sorted([i, hashmap[diff]])
        

        