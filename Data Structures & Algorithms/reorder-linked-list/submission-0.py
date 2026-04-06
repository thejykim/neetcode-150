# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None
        
        prev, pointer = None, middle

        # reverse second half
        while pointer:
            nxt = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = nxt
        
        # merge
        p1 = head
        p2 = prev

        while p1 and p2:
            nextp1 = p1.next
            nextp2 = p2.next

            p1.next = p2
            p2.next = nextp1

            p1 = nextp1
            p2 = nextp2
