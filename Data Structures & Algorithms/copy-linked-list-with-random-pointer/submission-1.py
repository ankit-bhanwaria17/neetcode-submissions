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
            return None
        hashmap = {} # key -> value : oldNode -> NewNode
        tempHead = head
        while tempHead:
            newNode = Node(tempHead.val)
            hashmap[tempHead] = newNode
            tempHead = tempHead.next
        tempHead = head
        while tempHead:
            newNode = hashmap[tempHead]
            newNode.next = hashmap[tempHead.next] if tempHead.next else None
            newNode.random = hashmap[tempHead.random] if tempHead.random else None
            tempHead = tempHead.next
        return hashmap[head]