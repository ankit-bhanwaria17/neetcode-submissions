# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum = 0
        l3 = ListNode()
        dummyHead = ListNode(0, l3)

        while l1 and l2:
            sum = l1.val + l2.val + carry
            l3.val = sum % 10
            carry = sum//10
            l3.next = ListNode(0, None)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum = l1.val + carry
            l3.val = sum%10
            carry = sum//10
            l3.next = ListNode(0, None)
            l3 = l3.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            l3.val = sum%10
            carry = sum//10
            l3.next = ListNode(0, None)
            l3 = l3.next
            l2 = l2.next

        if carry:
            l3.val = carry
            l3.next =  ListNode(carry, None)
        temp = dummyHead.next
        prev = None
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return dummyHead.next

