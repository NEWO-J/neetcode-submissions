# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthSmall = None
        # essentailyl what we need to do is go to the very bottom left, and then subtract from k each backtrack we do from there til we hit 0.
        def findNext(root):
            nonlocal k
            nonlocal kthSmall
            if not root:
                return False
            
            findNext(root.left)
            k -= 1
            if k == 0:
                kthSmall = root.val
            findNext(root.right)
            # subtract then pass back up.

            

        
        findNext(root)
        return kthSmall