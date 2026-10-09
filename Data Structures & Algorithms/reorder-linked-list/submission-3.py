# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodelist = []
        top = head
        while head:
            nodelist.append(head)
            head = head.next
        
        for i in range(len(nodelist)-1, (len(nodelist)//2)-1, -1):
            next1 = top.next
            top.next = nodelist[i]
            print(nodelist[i].val)
            top.next.next = next1
            if top.next:
                top = top.next.next
        
        top.next = None
