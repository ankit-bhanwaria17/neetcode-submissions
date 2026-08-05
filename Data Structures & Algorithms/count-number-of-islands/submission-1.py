class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island += 1
                    visited.add((i, j))
                    self.bfs(i, j, grid, visited)
        return island

    def bfs(self, r, c, grid, visited):
        q = deque()
        q.append((r, c))
        ROWS, COLS = len(grid), len(grid[0])
        while q:
            i, j = q.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                nr = i + dr
                nc = j + dc
                if (
                    nr in range(ROWS) 
                    and nc in range(COLS) 
                    and grid[i][j] == "1" 
                    and (nr, nc) not in visited
                ):
                    q.append((nr, nc))
                    visited.add((nr, nc))