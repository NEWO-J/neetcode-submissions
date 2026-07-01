class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        mindiff = float('inf')
        nsorted = sorted(nums)
        i = 0
        j = (k - 1)
        while j < len(nsorted):
            mindiff = min(nsorted[j] - nsorted[i], mindiff)
            i += 1
            j += 1
        
        return mindiff