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
