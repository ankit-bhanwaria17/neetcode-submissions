class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            result = None
            if j+1 < len(p) and p[j+1] == "*":
                result = (
                    dfs(i, j+2)
                    or (match and dfs(i+1, j))
                )
            elif match:
                result = dfs(i+1, j+1)
            else:
                result = False
            
            cache[(i, j)] = result
            return result

        return dfs(0, 0)