# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkNode(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 and n2 or not n2 and n1 or n1.val != n2.val:
                return False

            return checkNode(n1.left, n2.left) and checkNode(n1.right, n2.right)

        result = checkNode(p, q)  
        return result

