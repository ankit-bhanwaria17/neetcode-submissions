class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency = [[] for _ in range(n)]
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        visited = [False] * n
        components = 0

        for start in range(n):
            if visited[start]:
                continue
            # Iterative DFS uses stack
            # Recursive DFS uses the call stack
            components += 1
            visited[start] = True
            stack = [start]

            while stack:
                node = stack.pop()

                for neighbor in adjacency[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

        return components