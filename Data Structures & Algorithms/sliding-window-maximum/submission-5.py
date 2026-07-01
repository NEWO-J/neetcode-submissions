class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        result = []
        i = 0
        j = 0
        while j < k:
            while q and nums[j] > q[-1]:
                q.pop()
            q.append(nums[j])
            j += 1
        result.append(q[0])

        while j < len(nums):
            while q and nums[j] > q[-1]:
                q.pop()
            q.append(nums[j])
            j += 1
            if nums[i] == q[0]:
                q.popleft()
            i += 1
            result.append(q[0])
            
        

        return result