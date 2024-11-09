# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        start = ListNode()
        start2 = start
        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum > 9:
                sum -= 10
                carry = 1
            else:
                carry = 0
            start.next = ListNode(sum)
            start = start.next
            l1 = l1.next
            l2 = l2.next

        if l1 or l2:
            node = l1 or l2
            sum = carry + node.val
            if sum > 9:
                sum -= 10
                carry = 1
            else:
                carry = 0
            start.next = ListNode(sum)
            start = start.next
            node = node.next

        return start2.next 

            

