# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        head = dummy
        
        while l1 or l2:
            carry = 0
        
            if l2 and l1:
                sum = l1.val + l2.val
            elif l2:
                sum = l2.val
            else:
                sum = l1.val
       
            total_sum = dummy.val + sum
            dummy.val = total_sum % 10
            if total_sum >= 10:
                carry = 1

    
            dummy.next = ListNode(carry)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if not l1 and not l2 and dummy.next.val == 0:
                dummy.next = None


            dummy = dummy.next
        


        return head

            