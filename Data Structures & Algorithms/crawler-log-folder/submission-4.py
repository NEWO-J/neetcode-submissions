class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dirstack = []
        minlength = 0
        for operation in logs:
            match operation:
                case "../":
                    if dirstack:
                        dirstack.pop()
                        minlength -= 1
                case "./":
                    continue
                case _:
                    minlength += 1
                    dirstack.append(operation)

        
        return minlength