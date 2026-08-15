class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i, j): 
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            operations = 0
            if word1[i] == word2[j]:
                operations = dfs(i+1, j+1)
            else:
                operations = 1 + min(
                    dfs(i, j+1), # insert
                    dfs(i+1, j), # delete
                    dfs(i+1, j+1) # replace
                )
            cache[(i, j)] = operations
            return operations
        
        return dfs(0, 0)