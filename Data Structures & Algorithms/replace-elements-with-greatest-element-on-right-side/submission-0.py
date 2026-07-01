class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = greatest
            if current > greatest:
                greatest = current
            else:
                arr[i] = greatest
        arr[-1] = -1
        return arr
            
