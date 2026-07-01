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
                    if not stack or charmap[char] != stack.pop():
                        return False
            else:
                stack.append(char)
        
        return not stack
