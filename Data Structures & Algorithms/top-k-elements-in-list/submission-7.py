class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freqmap = [[] for _ in range(len(nums) + 1)]
        result = []
        for i in nums: 
            if i not in hashmap:
                hashmap[i] = 0
            
            hashmap[i] += 1

        for key,value in hashmap.items():
            freqmap[value].append(key)
        
        for i in range(len(freqmap) - 1, -1, -1):
            for val in freqmap[i]:
                result.append(val)
                if len(result) == k:
                    return result
            
