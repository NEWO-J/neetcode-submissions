# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        i = head
        j = head
        count_j = 0
        count_i = 0
        prev = None

        while j:
            j = j.next
            count_j += 1
        
        while count_i < (count_j - n):
            prev = i
            i = i.next
            count_i += 1
    

        if prev and i.next:
            prev.next = i.next
        elif i.next:
            return i.next
        elif prev:
            prev.next = None
        else:
            return None


            
        return head
        


        