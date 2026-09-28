# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        c, tracker = head, set()

        while c:
            if c.next in tracker:
                return True
            tracker.add(c)
            c = c.next
        return False
        