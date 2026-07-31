# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        i = head
        j = head.next

        while i and j:
            i = i.next
            j = j.next
            if j == None:
                return False
            j = j.next
            if i.next == j:
                return True


        return False
