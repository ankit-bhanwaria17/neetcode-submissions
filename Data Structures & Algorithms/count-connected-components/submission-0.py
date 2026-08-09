class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        processed = set()
        visited = set()
        total = 0
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in adj[node]:
                if i not in processed:
                    dfs(i)
            processed.add(node)

        for i in range(n):
            if i not in processed:
                dfs(i)
                total += 1
        return total