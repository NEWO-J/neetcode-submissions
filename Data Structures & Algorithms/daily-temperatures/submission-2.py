class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i,v in enumerate(temperatures):
                while stack and v > stack[-1][1]:
                        temp = stack.pop()
                        result[temp[0]] = i - temp[0]
                stack.append([i,v])

        return result