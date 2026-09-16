# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        unbalanced = False
        def balanced(root):
            nonlocal unbalanced
            if not root:
                return 0
            
            ldepth = balanced(root.left)
            rdepth = balanced(root.right)

            balance = ldepth - rdepth
            if balance > 1 or balance < -1:
                unbalanced = True

            return max(ldepth, rdepth) + 1
        
        balanced(root)
        return not unbalanced