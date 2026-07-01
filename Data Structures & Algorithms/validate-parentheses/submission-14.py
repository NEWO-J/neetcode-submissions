class Solution:
    def isValid(self, s: str) -> bool:
        pstack = []
        for c in s:
            match c:
                case "}":
                    if pstack and pstack[-1] == "{":
                        pstack.pop()
                    else: 
                        return False
                case "]":
                    if pstack and pstack[-1] == "[":
                        pstack.pop()
                    else:
                        return False
                case ")":
                    if pstack and pstack[-1] == "(":
                        pstack.pop()
                    else:
                        return False
                case _:
                    pstack.append(c)
        
        if pstack:
            return False
        else:
            return True