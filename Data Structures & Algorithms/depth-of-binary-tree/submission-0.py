# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        pointers = [root]
        seen = {}
        depth = 1
        max_depth = 0

        while pointers:
            left = pointers[-1].left
            right = pointers[-1].right
            if left and left not in seen:
                depth += 1
                pointers.append(left)
                seen[left] = True
            elif right and right not in seen:
                depth += 1
                pointers.append(right)
                seen[right] = True
            else:
                max_depth = max(depth, max_depth)
                depth -= 1
                pointers.pop()

        return max_depth