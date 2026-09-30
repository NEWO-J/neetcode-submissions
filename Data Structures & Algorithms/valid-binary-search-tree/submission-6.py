# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        rootval = root.val
        valid = True
        def isValid(root, low, high):
            nonlocal rootval
            nonlocal valid
            if not root or not valid:
                return
            if root.val <= low or root.val >= high:
                valid = False
                return

            isValid(root.right, root.val, high)
            isValid(root.left, low, root.val)
      
        isValid(root, float('-inf'), float('inf'))
        return valid