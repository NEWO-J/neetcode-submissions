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
        if not head:
            return None

        dummy = Node(-1)

        cur = head
        dummy.next = Node(head.val)
        dummyhead = dummy
        dummy = dummy.next

        hmap = collections.defaultdict(int)
        hmap2 = collections.defaultdict(int)

        while cur:
            hmap2[cur] = dummy
            dummy.val = cur.val
            if cur.next:
                dummy.next = Node(cur.next.val)

            if cur in hmap:
                for pointer in hmap[cur]:
                    pointer.random = dummy

            if cur.random:
                if cur.random in hmap2:
                    dummy.random = hmap2[cur.random]
                else:
                    print(cur.random.val)
                    print("attached to")
                    print(dummy.val)
                    if cur.random in hmap:
                        hmap[cur.random].append(dummy)
                    else:
                        hmap[cur.random] = [dummy]

            cur = cur.next
            dummy = dummy.next
        
        return dummyhead.next




             