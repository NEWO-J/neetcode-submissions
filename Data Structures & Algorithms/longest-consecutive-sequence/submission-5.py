class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # $O(n)$ to build
        longest_streak = 1
        
        if not num_set:
            return 0
        for num in num_set:
            # Check if the previous number exists in the set
            if (num - 1)  not in set(nums):
                  current_streak = 1
                  current_num = num
                  while (current_num + 1) in set(nums):
                    current_num += 1
                    current_streak += 1
                    if current_streak > longest_streak:
                        longest_streak = current_streak

        return longest_streak

