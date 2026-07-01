class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dirstack = []
        minlength = 0
        for operation in logs:
            match operation:
                case "../":
                    if dirstack:
                        dirstack.pop()
                        
                case "./":
                    continue
                case _:
                    dirstack.append(operation)

        
        return len(dirstack)