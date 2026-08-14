class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            count = 0
            for k in range(i, len(s)):
                if s[k] == t[j]:
                    count += dfs(k+1, j+1)

            cache[(i, j)] = count
            return count
        
        return dfs(0, 0)