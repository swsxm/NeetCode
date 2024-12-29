class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kElem = self.getKGroup(groupPrev, k)
            if not kElem:
                break
            groupNext = kElem.next

            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kElem
            groupPrev = tmp

        return dummy.next

    def getKGroup(self, head, k):
        while head and k > 0:
            head = head.next
            k -= 1
        return head if k == 0 else None
