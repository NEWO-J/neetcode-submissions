class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        freqmap = [[] for _ in range(len(nums))]
        result = []
        for i in nums:
            freq[i] += 1

        for key,value in freq.items():
            freqmap[value - 1].append(key)

        
        for i in range(len(freqmap)-1, -1, -1):
            if freqmap[i]:
                for element in freqmap[i]:
                    result.append(element)
                    if len(result) == k:
                        return result

        return result
        
            