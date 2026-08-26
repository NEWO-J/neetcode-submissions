class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums1) - 1

        partlen = ((len(nums1) + len(nums2)) // 2)

        while True:
            i = (l + r) // 2
            j = (partlen - i) - 2

            AL = nums1[i] if i >= 0 else float("-inf")
            AR = nums1[i + 1] if (i + 1) < len(nums1) else float("inf")
            BL = nums2[j] if j >= 0 else float("-inf")
            BR = nums2[j+1] if (j+1) < len(nums2) else float("inf")
            
            if AL <= BR and BL <= AR:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(AL, BL) + min(AR, BR)) / 2
                else:
                    return min(AR, BR)
            elif AL > BR:
                r = i - 1
            else:
                l = i + 1
       
          
            

