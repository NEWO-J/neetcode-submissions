class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = collections.defaultdict(int)
        pairs = len(nums) / 2
        for i in nums:
            hashmap[i] += 1
        
        for key,value in hashmap.items():
            if value % 2 == 1:
                return False


        return True
