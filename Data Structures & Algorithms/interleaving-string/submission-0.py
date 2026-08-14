class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {}
        def dfs(i, j, k, res):
            if k == len(s3):
                return True if "".join(res) == s3 else False
            
            if (i, j) in cache:
                return cache[(i, j)]

            temp = False
            if i < len(s1) and s3[k] == s1[i]:
                res.append(s1[i])
                temp = dfs(i+1, j, k+1, res)
                res.pop()
            if j < len(s2) and s3[k] == s2[j]:
                res.append(s2[j])
                temp = temp or dfs(i, j+1, k+1, res)
                res.pop()

            cache[(i, j)] = temp
            return temp

        return dfs(0, 0, 0, [])           
