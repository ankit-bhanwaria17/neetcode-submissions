# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        previousGroupTail = dummyHead

        while True:
            # Check whether a complete group of k nodes remains.
            groupTail = previousGroupTail
            for _ in range(k):
                groupTail = groupTail.next
                if groupTail is None:
                    return dummyHead.next

            originalGroupHead = previousGroupTail.next
            nextGroupHead = groupTail.next

            # Reverse this group and connect its tail to the next group.
            previous = nextGroupHead
            current = originalGroupHead
            for _ in range(k):
                nextNode = current.next
                current.next = previous
                previous = current
                current = nextNode

            # The original head is now this group's tail.
            previousGroupTail.next = groupTail
            previousGroupTail = originalGroupHead