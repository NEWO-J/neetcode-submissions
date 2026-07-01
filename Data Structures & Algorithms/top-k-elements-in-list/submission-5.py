class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        most_frequent = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
            
        for i in hash_table:
            most_frequent[hash_table[i]].append(i)
        
        for i in range(len(most_frequent) -1, -1, -1):
            for num in most_frequent[i]:
                result.append(num)
            if len(result) == k:
                return result