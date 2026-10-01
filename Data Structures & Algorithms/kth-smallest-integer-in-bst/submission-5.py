# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthSmall = None
        def findNext(root):
            nonlocal k
            nonlocal kthSmall
            if not root:
                return
            
            findNext(root.left)
            k -= 1
            if k == 0:
                kthSmall = root.val
                return
            if kthSmall:
                return
            findNext(root.right)

        
        findNext(root)
        return kthSmall