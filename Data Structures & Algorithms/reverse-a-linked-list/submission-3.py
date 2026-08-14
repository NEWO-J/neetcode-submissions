# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        

        current = head
        next = current.next
        current.next = None
        prev = current
        current = next

        while current.next:
            next = current.next
            current.next = prev
            prev = current
            current = next

        current.next = prev
        return current