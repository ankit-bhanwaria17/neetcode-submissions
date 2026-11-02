# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        dummyHead = head
        while dummyHead:
            dummyHead = dummyHead.next
            size += 1
        dummyHead = ListNode(0, head)
        prev = dummyHead
        curr = head
        lenToTraverse = size - n
        while lenToTraverse > 0:
            prev = curr
            curr = curr.next
            lenToTraverse -= 1
        prev.next = curr.next
        curr.next = None
        return dummyHead.next