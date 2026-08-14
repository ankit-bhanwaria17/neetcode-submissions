class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        result = 1
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            path = []
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in direction:
                nr = dr+i
                nc = dc+j
                if (
                    0 <= nr < len(matrix) and
                    0 <= nc < len(matrix[0]) and
                    matrix[nr][nc] > matrix[i][j]
                ):
                    path.append(dfs(nr, nc))
            
            cache[(i, j)] = 1 + max(path) if path else 1
            return cache[(i, j)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, dfs(i, j))
        return result