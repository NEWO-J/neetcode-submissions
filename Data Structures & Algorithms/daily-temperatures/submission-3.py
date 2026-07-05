class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monstack = []
        output = [0 for _ in range(len(temperatures))]

        for i,v in enumerate(temperatures):
            while monstack and v > monstack[-1][1]:
                lastval = monstack.pop()
    
                output[lastval[0]] = i - lastval[0] 
            
            monstack.append((i,v))
        
        return output
