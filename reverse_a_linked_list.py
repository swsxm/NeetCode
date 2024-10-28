from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursiv(prev, curr):
            if not curr:
                return prev
            next = curr.next
            curr.next = prev
            return recursiv(curr, next)
        
        return recursiv(None, head)
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            next = curr.next
            curr.next = prev
            curr = next

        return prev

