class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:   
        nums = sorted(nums)
        n = len(nums) - 1

        result = []
        print(nums)
        for i in range(n):
            j = i + 1
            k = n
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            while j < k:
                if k == i:
                    k -= 1
                
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                
                    while j < n and nums[j] == nums[j - 1]:
                        j += 1
            
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1
                
        return result


            