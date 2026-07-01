class Solution:
    def isValid(self, s: str) -> bool:
        charmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = [] 
        for char in s:
            if char in charmap:
                if stack:
                    if charmap[char] == stack[-1]:
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            else:
                stack.append(char)
            
        if stack:
            return False
        
        return True
