class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dirstack = []
        depth = 0
        for operation in logs:
            match operation:
                case "../":
                    if depth > 0:
                        depth -= 1
                case "./":
                    continue
                case _:
                    depth += 1

        return depth