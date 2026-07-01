class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        streak = 0
        best_streak = 0
        for num in nums:
            if num - 1 not in nums:
                streak = 1
                currentnum = num
                while currentnum + 1 in nums:
                    currentnum += 1 
                    streak += 1
                    if streak > best_streak:
                        best_streak = streak
            if streak > best_streak:
                        best_streak = streak
        
        return best_streak