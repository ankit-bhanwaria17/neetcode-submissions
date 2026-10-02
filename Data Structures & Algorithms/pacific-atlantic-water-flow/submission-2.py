class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(starts):
            visited = set(starts)
            queue = deque(visited)

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return visited

        pacific_starts = (
            [(0, c) for c in range(cols)]
            + [(r, 0) for r in range(rows)]
        )
        atlantic_starts = (
            [(rows - 1, c) for c in range(cols)]
            + [(r, cols - 1) for r in range(rows)]
        )

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r, c] for r, c in pacific & atlantic]