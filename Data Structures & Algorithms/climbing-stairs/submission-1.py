class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {}
        def dfs(i):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return 1
            if i in memory:
                return memory[i]
            memory[i] = dfs(i-1) + dfs(i-2)
            return memory[i]
        return dfs(n)