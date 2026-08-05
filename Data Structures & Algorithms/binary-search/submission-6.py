class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1


        while l < r:
            midpoint = (l + r) // 2

            if nums[midpoint] > target:
                r = midpoint
            elif nums[midpoint] < target:
                l = midpoint + 1
            else:
                return midpoint

        if nums[l] == target:
            return l
        else:
            return -1