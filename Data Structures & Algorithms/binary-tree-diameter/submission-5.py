# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        
        maxtotal = 0
        def diam(root):
            nonlocal maxtotal
            
            if not root:
                return 0
            
            left = diam(root.left)
            right = diam(root.right)

            total = left + right
            maxtotal = max(total, maxtotal)

            return max(left + 1, right + 1)

        diam(root)
        return maxtotal