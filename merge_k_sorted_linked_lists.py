# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        start = dummy = ListNode()
        while True:
            smallest_head = None
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                if smallest_head is None:
                    smallest_head = i
                else:
                    smallest_head = (
                        smallest_head if lists[smallest_head].val < lists[i].val else i
                    )

            if smallest_head is None:
                return start.next
            else:
                dummy.next = lists[smallest_head]
                dummy = dummy.next
                lists[smallest_head] = lists[smallest_head].next

    # merge sort divide and conquer approach
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
