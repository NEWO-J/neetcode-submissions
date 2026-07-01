class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap and i != hashmap[diff]:
                return sorted([i, hashmap[diff]])

            hashmap[nums[i]] = i
        

        