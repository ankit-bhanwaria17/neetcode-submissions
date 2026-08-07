class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    pacific.add((i, j))
                if i == ROWS-1 or j == COLS-1:
                    atlantic.add((i, j))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque(list(pacific))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (
                    nr in range(ROWS)
                    and nc in range(COLS)
                    and (nr, nc) not in pacific
                    and heights[nr][nc] >= heights[r][c]
                ):
                    pacific.add((nr, nc))
                    q.append((nr, nc))
        q = deque(list(atlantic))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (
                    nr in range(ROWS)
                    and nc in range(COLS)
                    and (nr, nc) not in atlantic
                    and heights[nr][nc] >= heights[r][c]
                ):
                    atlantic.add((nr, nc))
                    q.append((nr, nc))
        result = []
        for cell in atlantic:
            if cell in pacific:
                result.append(list(cell))
        return result
