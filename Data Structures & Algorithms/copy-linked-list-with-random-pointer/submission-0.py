"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        table = dict()

        prev, pointer = None, head

        while pointer:
            table[pointer] = Node(pointer.val)

            if prev:
                table[prev].next = table[pointer]

            prev = pointer
            pointer = pointer.next
        
        pointer = head

        while pointer:
            if pointer.random:
                table[pointer].random = table[pointer.random]
            pointer = pointer.next
        
        return table[head]