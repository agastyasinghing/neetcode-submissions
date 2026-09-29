# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        curr, s.next, prev = s.next, None, None
        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
        first, second = head, prev
        while first and second:
            nextfirst = first.next
            nextsecond = second.next
            first.next = second
            second.next = nextfirst
            first = nextfirst
            second = nextsecond
        
       
        


        