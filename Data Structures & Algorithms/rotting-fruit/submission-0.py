class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        t = 0
        while q:
            r, c, t = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if (
                    nr in range(len(grid))
                    and nc in range(len(grid[0]))
                    and grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    q.append((nr, nc, t+1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    t = -1
                    break
        return t
