class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monostack = collections.deque()
        monostack.append(nums[0])
        result = []
        if k == 1:
            return nums

        i = 0
        j = 1
        while j < k - 1:
            while monostack and nums[j] > monostack[-1]:
                monostack.pop()
            monostack.append(nums[j])
            j += 1

        while j < len(nums):
            while monostack and nums[j] > monostack[-1]:
                monostack.pop()
            monostack.append(nums[j])

            result.append(monostack[0])

            if nums[i] == monostack[0]:
                monostack.popleft()

            i += 1
            j += 1

        return result

            