class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = []
        arr2 = [0 for _ in range(len(nums))]
        result = []
        total = 1
        
        for i in range(n - 1, -1, -1):
            total *= nums[i]
            arr2[i] = total
        total = 1
        for i in range(n):
            total *= nums[i]
            arr1.append(total)
            if i > 0 and i < n - 1:
                result.append(arr1[i - 1] * arr2[i + 1])
            elif i == 0:
                result.append(arr2[1])
            else:
                result.append(arr1[-2])
        
        return result