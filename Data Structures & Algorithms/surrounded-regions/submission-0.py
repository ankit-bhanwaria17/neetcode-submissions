class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if (
                    i == 0 or i == rows-1 
                    or j == 0 or j == cols-1
                ):
                    if board[i][j] == "O":
                        board[i][j] = "#"
                        q.append([i, j])
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
        while q:
            r, c = q.popleft()
            for dr, dc in dir:
                nr, nc = dr + r, dc + c
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] == "O"
                ):
                    board[nr][nc] = "#"
                    q.append([nr, nc]) 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"


                    