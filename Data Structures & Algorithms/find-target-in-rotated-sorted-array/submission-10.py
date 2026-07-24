class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1

        while l < r:
            midpoint = (l + r) // 2
            print(l)
            print(r)
            if nums[r] < nums[midpoint]:
                print("left half is sorted")
                if nums[l] <= target < nums[midpoint]:
                    r = midpoint - 1
                elif nums[midpoint] == target:
                    return midpoint
                else:
                    print("target in right half")
                    l = midpoint + 1
            else:
                print("right half is sorted")
                if nums[midpoint] < target <= nums[r]:
                    print("moving left in")
                    l = midpoint + 1
                elif nums[midpoint] == target:
                    return midpoint
                else:
                    print("moving right in")
                    r = midpoint - 1
                


    
        if nums[r] == target:
            return r
        else:
            return -1
