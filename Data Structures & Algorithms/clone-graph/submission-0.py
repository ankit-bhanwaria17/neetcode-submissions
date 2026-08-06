"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {} # node: clone
        def dfs(root):
            if not root:
                return
            if root in visited:
                return visited[root]
            clone = Node(root.val, [])
            visited[root] = clone
            for n in root.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)

