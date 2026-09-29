# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        monstack = [root.val]
        def search(root, greatest):
            nonlocal count
            if not root:
                return
            if root.val >= greatest:
                greatest = root.val
                count += 1
                
            search(root.left, greatest)
            search(root.right, greatest)

        search(root, root.val)
        return count
