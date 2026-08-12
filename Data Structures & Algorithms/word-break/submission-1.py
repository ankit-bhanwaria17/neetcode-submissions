class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * (len(s)+1)
        wordSet = set(wordDict)
        def dfs(i):        
            if i == len(s):
                return True
            if dp[i] is not None:
                return dp[i]
            res = False
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    res = res or dfs(j+1)
            dp[i] = res
            return res
        return dfs(0)