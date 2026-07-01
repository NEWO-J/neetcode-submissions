class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 1
        while j < len(nums):
            if (j - i) <= k:
                if nums[i] == nums[j]:
                    return True
            else:
                i += 1
                j = i
            j += 1
        return False
   