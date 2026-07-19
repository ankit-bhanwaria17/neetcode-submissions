"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummyHead = Node(0, head, None)
        # A -> A' -> B -> B' -> C -> C'
        while head:
            newNode = Node(head.val)
            nextNode = head.next
            head.next = newNode
            newNode.next = nextNode
            head = nextNode
        
        # connect random node
        h1 = dummyHead.next
        h2 = h1.next
        while h2.next:
            h2.random = h1.random.next if h1.random else None
            h1 = h1.next.next
            h2 = h2.next.next
        h2.random = h1.random.next if h1.random else None
        # Seprate
        h1 = dummyHead.next
        h2 = h1.next
        result = h2
        while h2.next:
            nextH1 = h1.next.next
            nextH2 = h2.next.next
            h1.next = nextH1
            h2.next = nextH2
            h1 = nextH1
            h2 = nextH2
        h1.next = None
        return result

        