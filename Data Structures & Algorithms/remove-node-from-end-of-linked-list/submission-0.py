# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        c, p, nc = head, None, head
        count, c2 = 0, 0
        while c:
            c = c.next
            count += 1
        target = (count - n) 
        if target == 0:
            head = head.next
        else:
            while nc:
                if (c2 == target):
                    prev.next = nc.next
                c2 += 1
                prev = nc
                nc = prev.next
                
            
            
        return head
            






        