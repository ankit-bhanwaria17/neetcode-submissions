class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # Pattern is finished
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == ".")
            )

            # Case 1: next character in pattern is '*'
            if j + 1 < len(p) and p[j + 1] == "*":
                result = (
                    dfs(i, j + 2)              # use * zero times
                    or
                    (match and dfs(i + 1, j))  # use * one or more times
                )

            # Case 2: normal character or '.'
            else:
                result = match and dfs(i + 1, j + 1)

            cache[(i, j)] = result
            return result

        return dfs(0, 0)