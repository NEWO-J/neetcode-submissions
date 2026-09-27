# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxDepth = -1
        curBest = None

        def lowestCom(root, depth):
            nonlocal maxDepth
            nonlocal curBest
            current = False
            if not root:
                return 
                
            if root == p or root == q:
                current = True

            right = lowestCom(root.right, depth + 1)
            print(right)
            left = lowestCom(root.left, depth + 1)
            print(left)

            # valid subtree
            if (current or left) and right or (current or right) and left:
                if depth > maxDepth:
                    maxDepth = depth
                    curBest = root
            
            # logic for returning a valid branch containing p or q
            return current or right or left
            
        lowestCom(root, 0)
        return curBest