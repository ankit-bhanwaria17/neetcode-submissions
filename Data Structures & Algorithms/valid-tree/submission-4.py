class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        seen = set([0])
        q = deque([0])
        while q:
            currNode = q.popleft()
            for i in adj[currNode]:
                if i not in seen:
                    q.append(i)
                    seen.add(i)
        return len(seen) == n