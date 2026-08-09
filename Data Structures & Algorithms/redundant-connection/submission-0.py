class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Topological Sort
        n = len(edges)
        degree = [0]*(n+1)
        adj = {i: [] for i in range(1, n+1)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            degree[n1] += 1
            degree[n2] += 1
        q = deque()
        for i in range(1, len(degree)):
            if degree[i] == 1:
                q.append(i)
        while q:
            node = q.popleft()
            degree[node] -= 1
            for i in adj[node]:
                degree[i] -= 1
                if degree[i] == 1:
                    q.append(i)
        
        for n1, n2 in reversed(edges):
            if degree[n1] == 2 and degree[n2] == 2:
                return [n1, n2]
        return []
