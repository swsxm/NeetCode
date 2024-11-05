# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return head
        slow, fast = head, head.next

        # find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        right_side = slow.next
        prev = slow.next = None

        # reverse right side
        while right_side:
            tmp = right_side.next
            right_side.next = prev
            prev = right_side
            right_side = tmp

        right_side = prev
        left_side = head

        while left_side and right_side:
            tmp = left_side.next
            left_side.next = right_side
            left_side = tmp

            tmp2 = right_side.next
            right_side.next = left_side
            right_side = tmp2
        
        return head
    
