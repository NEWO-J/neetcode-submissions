# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        deq = collections.deque()
        deq.append(root)
        deqnew = collections.deque()
        result = []
        result.append(deq[-1].val)

        while deq:
            for node in range(len(deq)):
                removed = deq.popleft()
                if removed.left:
                    deq.append(removed.left)
                if removed.right:
                    deq.append(removed.right)

            if deq:
                result.append(deq[-1].val)

        
        return result

            


