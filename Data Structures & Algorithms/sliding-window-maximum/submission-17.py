class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi = collections.deque()
        result = []

        for j in range(k):
            while maxi and maxi[-1][1] < nums[j]:
                maxi.pop()
            maxi.append((j, nums[j]))
            

        result.append(maxi[0][1])
    

        i = 1
        j = k
        while j < len(nums):
            while maxi and maxi[-1][1] < nums[j]:
                maxi.pop()
            maxi.append((j, nums[j]))
            while maxi[0][0] < i:
                maxi.popleft()
            
            result.append(maxi[0][1])

            i += 1
            j += 1


        return result