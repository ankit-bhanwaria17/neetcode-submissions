class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        size = [1]*(n+1)
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            if size[pa] > size[pb]:
                pa, pb = pb, pa
            parent[pa] = pb
            size[pb] += size[pa]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        
        return []