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
        curr = head
        hashmap = {}
        while curr:
            new = Node(curr.val)
            hashmap[curr] = new
            curr = curr.next

        curr = head
        while curr:
            hashmap[curr].next = hashmap.get(curr.next)
            hashmap[curr].random = hashmap.get(curr.random)
            curr = curr.next
        return hashmap[head] if head else None

            
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        head_copy = curr.next

        while curr:
            tmp = curr.next
            curr.next = tmp.next
            curr = curr.next
        
        return head_copy
