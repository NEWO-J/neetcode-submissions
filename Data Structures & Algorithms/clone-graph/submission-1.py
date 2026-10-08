"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nstack = collections.deque([node])
        visited = {}
        clone = Node(node.val)
        head = clone
        visited[node] = clone
        while nstack:  
            prev = nstack.popleft()
            clone = visited[prev]
            for neighbor in prev.neighbors:
                if neighbor in visited:
                    clone.neighbors.append(visited[neighbor])
                else:
                    clone.neighbors.append(Node(neighbor.val))
                    visited[neighbor] = clone.neighbors[-1] 
                    nstack.append(neighbor)
            

        return head
