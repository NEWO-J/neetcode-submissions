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
        def search(root, monstack):
            nonlocal count
            added = False
            if not root:
                return
            if root.val >= monstack[-1]:
                monstack.append(root.val)
                count += 1
                added = True

            search(root.left, monstack)
            search(root.right, monstack)

            if added:
                monstack.pop()

        search(root, monstack)
        return count
