class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # what do we store in the stack?
        # When do we remove from the stack?
        # When do we add to the stack?
        stack = []
        result = [0 for i in range(len(temperatures))]
        for i, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            stack.append(i)
        
        return result