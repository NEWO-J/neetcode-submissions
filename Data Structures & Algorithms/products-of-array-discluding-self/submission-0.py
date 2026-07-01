class Solution:
    # If self not in hashmap
    # Add hashmap
    # the sum of all elements divided by current element 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        totalwithnozero = 1
        zerocount = 0
        result = []
        for num in nums:
            if num == 0:
                zerocount += 1
                if zerocount > 1:
                    totalwithnozero = totalwithnozero * 0
            elif zerocount <= 1:
                totalwithnozero = totalwithnozero * num

            total = total * num
        for num in nums:
            if num == 0 and zerocount <= 1:
                result.append(int(totalwithnozero))
            elif num == 0:
                result.append(0)
            else:
                result.append(int(total / num))

        return result
