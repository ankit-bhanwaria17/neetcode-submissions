class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if self.isValidQueenPlacement(board, r, c):
                    board[r][c] = "Q"
                    dfs(r+1)
                    board[r][c] = "."
        dfs(0)
        return result

    def isValidQueenPlacement(self, board, r, c):
        row = r-1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        
        row, col = r-1, c-1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        
        row, col = r-1, c+1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True

