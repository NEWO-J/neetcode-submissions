class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0

        while len(nums) > 1:
            midpoint = len(nums) // 2
            first_half = nums[:midpoint]
            second_half = nums[midpoint:]

            if second_half[0] > target:
                nums = first_half
            else:
                nums = second_half
                index += len(first_half)

        if nums[0] == target:
            return index
        else:
            return -1