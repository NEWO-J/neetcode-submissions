# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        maxdepth = 0
        def totalDepth(root):
            nonlocal maxdepth
            if root is None:
                return 0

            left = totalDepth(root.left)
            right = totalDepth(root.right)
            total_depth = (left + right) + 1
            maxdepth = max(total_depth - 1, maxdepth)
            return max(left + 1, right + 1)
        
        totalDepth(root)
        return maxdepth