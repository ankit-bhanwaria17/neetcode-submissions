class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: set() for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].add(n2)
            adjList[n2].add(n1)
        visited = set()
        def dfs(node, parentNode):
            if node in visited:
                return False
            visited.add(node)
            for i in adjList[node]:
                if i == parentNode:
                    continue
                if not dfs(i, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n




