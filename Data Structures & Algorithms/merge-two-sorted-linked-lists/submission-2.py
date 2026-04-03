# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2, res, head = list1, list2, None, None
        
        if not p1 and not p2:
            return head
        elif not p1 or (p2 and p1.val > p2.val):
            res, head = p2, p2
            p2 = p2.next
        else:
            res, head = p1, p1
            p1 = p1.next

        while p1 or p2:
            if not p1 or (p2 and p1.val > p2.val):
                res.next = p2
                res = res.next
                p2 = p2.next
            else:
                res.next = p1
                res = res.next
                p1 = p1.next
        
        return head
