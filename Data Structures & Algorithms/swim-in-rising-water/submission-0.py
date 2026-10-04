class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        best = [[float("inf")] * n for _ in range(n)]
        best[0][0] = grid[0][0]

        heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            time, row, col = heapq.heappop(heap)

            # A better route may have been found since this was pushed.
            if time > best[row][col]:
                continue

            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < n and 0 <= nc < n):
                    continue

                next_time = max(time, grid[nr][nc])

                if next_time < best[nr][nc]:
                    best[nr][nc] = next_time
                    heapq.heappush(heap, (next_time, nr, nc))
