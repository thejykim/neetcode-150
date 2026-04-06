# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find size of list
        pointer = head
        length = 0

        while pointer:
            length += 1
            pointer = pointer.next
        
        pointer = head
        step_size = length - n - 1

        if step_size < 0:
            return head.next

        for _ in range(step_size):
            pointer = pointer.next

        pointer.next = pointer.next.next

        return head