class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = []
        for _ in range(row):
            temp = []
            for _ in range(col):
                temp.append(False)
            visited.append(temp)
        startI = []
        startJ = []
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    startI.append(i)
                    startJ.append(j)

        if not startI:
            return False

        def dfs(i, j, index, visited):
            if index > len(word)-1:
                return True
            
            top = bottom = right = left = False
            if i > 0 and board[i-1][j] == word[index] and not visited[i-1][j]:
                visited[i-1][j] = True
                top = dfs(i-1, j, index+1, visited)
                visited[i-1][j] = False
            if i < row-1 and board[i+1][j] == word[index] and not visited[i+1][j]:
                visited[i+1][j] = True
                bottom = dfs(i+1, j, index+1, visited)
                visited[i+1][j] = False
            if j > 0 and board[i][j-1] == word[index] and not visited[i][j-1]:
                visited[i][j-1] = True
                left = dfs(i, j-1, index+1, visited)
                visited[i][j-1] = False
            if j < col-1 and board[i][j+1] == word[index] and not visited[i][j+1]:
                visited[i][j+1] = True
                right = dfs(i, j+1, index+1, visited)
                visited[i][j+1] = False

            return top or bottom or right or left
        
        for k in range(len(startI)):
            visited[startI[k]][startJ[k]] = True
            if dfs(startI[k], startJ[k], 1, visited):
                return True
            visited[startI[k]][startJ[k]] = False
        return False
