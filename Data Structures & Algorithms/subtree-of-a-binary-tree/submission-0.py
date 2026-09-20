# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:     
        isSubT = False
        def isSameTree(p, q):
            if not p and not q:
                return True

            if not p or not q or p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def isSub(root):
            nonlocal subRoot
            nonlocal isSubT
            if not root:
                return

            if isSameTree(root, subRoot):
                isSubT = True
            
            isSub(root.left)
            isSub(root.right)

        isSub(root)
        return isSubT