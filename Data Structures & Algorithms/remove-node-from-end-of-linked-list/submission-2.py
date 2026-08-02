# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.count = 0

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return None
        head.next = self.removeNthFromEnd(head.next, n)
        self.count += 1 
        if self.count == n:
            return head.next
        return head


        