class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for _ in range(len(nums) + 1)]
        result = []
        hmap = collections.defaultdict(int)
        n = len(nums) - 1

        for num in nums:
            hmap[num] += 1

        for key,value in hmap.items():
            frequencies[value].append(key)

        i = 0
        m = -1
        while i < k:
            for val in frequencies[m]:
                i += 1
                result.append(val)
            m -= 1

        return result