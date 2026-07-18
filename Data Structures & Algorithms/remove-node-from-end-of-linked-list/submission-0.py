# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        pos = size - n
        prev = None
        curr = head
        while pos > 0:
            pos -= 1
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            head = curr.next
        return head