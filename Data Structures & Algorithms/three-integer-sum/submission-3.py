class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while r > l and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1

        return result