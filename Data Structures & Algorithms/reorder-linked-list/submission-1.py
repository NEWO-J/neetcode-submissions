# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_stack = []
        start = head
        current = head

        if current.next is None:
            return None

        while current:
            list_stack.append(current)
            current = current.next
        
        current = start
        
        for i in range(len(list_stack)-1, len(list_stack)//2 - 1, -1):
            next = current.next
            print(current.val)
            current.next = list_stack[i]
            list_stack.pop()
            current.next.next = next
            current = current.next.next
        
        current.next = None
    


        return None
        