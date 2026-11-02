# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        l, r = dummyHead, head
        while n > 0:
            r = r.next
            n -= 1
        while r:
            l = l.next
            r = r.next
        # now l is just one node behind the node that needs to be removed
        l.next = l.next.next
        return dummyHead.next