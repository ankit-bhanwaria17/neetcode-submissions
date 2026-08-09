class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: set() for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].add(n2)
            adjList[n2].add(n1)
        visited = set()
        processed = set()
        print(adjList)
        def dfs(node, parentNode):
            if node in visited and node != parentNode:
                return False
            if node in processed:
                return True
            visited.add(node)
            for i in adjList[node]:
                if i == parentNode:
                    continue
                if not dfs(i, node):
                    return False
            visited.remove(node)
            processed.add(node)
            return True

        if not dfs(0, -1):
            return False
        return len(processed) == n




