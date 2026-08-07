class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    pacific.add((i, j))
                if i == ROWS-1 or j == COLS-1:
                    atlantic.add((i, j))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(visited):
            q = deque(list(visited))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited

        return [cell for cell in bfs(pacific) & bfs(atlantic)]
