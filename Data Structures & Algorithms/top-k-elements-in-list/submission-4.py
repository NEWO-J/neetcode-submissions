class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        hash_table[-999999999999999999999] = 0
        most_frequent = [-999999999999999999999] * k

        for num in nums:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
            
            for i in range(k):
                if hash_table[num] > hash_table[most_frequent[i]] and num not in most_frequent:
                    most_frequent[i] = num
        
        return most_frequent