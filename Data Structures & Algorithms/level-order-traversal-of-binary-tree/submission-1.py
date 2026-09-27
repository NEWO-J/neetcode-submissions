# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        if not root:
            return []
        result = [[root.val]]

        while queue:
            built = []
            for _ in range(len(queue)):
                removed = queue.popleft()
                if removed.left:
                    queue.append(removed.left)
                    built.append(removed.left.val)
                if removed.right:
                    queue.append(removed.right)
                    built.append(removed.right.val)

            if built:
                result.append(built[:])

        
        return result