"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:

  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    visited = {}

    def copy(node):
      # base case (begin waking up the recursion)
      if not node:
        return None
      # if we have seen the node, we instantly return it
      if node in visited:
        return visited[node]

      # copy the current node val to our new node
      new_node = Node(node.val)
      # logically map the old node to the new node via hashmap
      visited[node] = new_node

      new_node.next = copy(node.next)
      new_node.random = copy(node.random)

      return new_node

    return copy(head)




