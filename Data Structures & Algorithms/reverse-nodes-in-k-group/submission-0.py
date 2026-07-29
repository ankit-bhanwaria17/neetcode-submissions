# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        prevGroupTail = dummyHead

        while True:
            kth = prevGroupTail
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummyHead.next
            
            groupHead = curr = prevGroupTail.next
            prev = kth.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            prevGroupTail.next = prev
            prevGroupTail = groupHead
                    