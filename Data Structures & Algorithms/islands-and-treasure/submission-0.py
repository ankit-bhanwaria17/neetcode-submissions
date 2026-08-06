class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    continue
                q.append((i, j, 0))
        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (
                    nr in range(len(grid))
                    and nc in range(len(grid[0]))
                    and grid[nr][nc] == 2147483647
                ):
                    grid[nr][nc] = dist + 1
                    q.append((nr, nc, dist + 1))

