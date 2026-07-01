class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for r in range(len(nums)):
            if r > k:
                window.remove(nums[r - k - 1])

            if nums[r] in window:
                return True
            else:
                window.add(nums[r])
                
        return False
   