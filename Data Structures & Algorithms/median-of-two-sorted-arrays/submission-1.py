class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        if len(nums3) % 2 == 1:
             return nums3[(n // 2)]
        else:
            print(nums3)
            print(nums3[n // 2])
            return (nums3[(n // 2) - 1] + nums3[(n // 2)]) / 2

          
