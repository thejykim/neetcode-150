# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            kth = self.getKthNode(prev_group, k)
            if not kth:
                break
            
            group_start, group_next = prev_group.next, kth.next

            pointer, prev = prev_group.next, None

            while prev != kth:
                nxt = pointer.next
                pointer.next = prev
                prev = pointer
                pointer = nxt
            
            group_start.next = group_next
            prev_group.next = kth
            prev_group = group_start

        return dummy.next
        
    def getKthNode(self, prev_group: ListNode, k: int) -> Optional[ListNode]:
        pointer, step = prev_group, 0

        while step < k:
            step += 1
            pointer = pointer.next
            if not pointer:
                return None
        
        return pointer