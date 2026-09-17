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

            total_depth = (totalDepth(root.left)) + (totalDepth(root.right)) + 1
            print(total_depth)
            maxdepth = max(total_depth - 1, maxdepth)
            return max(totalDepth(root.left) + 1, totalDepth(root.right) + 1)
        
        totalDepth(root)
        return maxdepth