# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.count = 0

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        j = head
        start = head
        prev = None
        for _ in range(n):
            i = i.next
        while i:
            i = i.next
            prev = j
            j = j.next

        if j.next and prev:
            prev.next = j.next
        elif not prev:
            return head.next
        elif not j.next:
            prev.next = None

        return start

        