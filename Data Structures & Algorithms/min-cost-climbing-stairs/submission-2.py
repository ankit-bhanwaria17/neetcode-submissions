class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {0: 0, 1: 0}
        def dfs(i):
            if i in cache:
                return cache[i]
            cache[i] = min(
                dfs(i-1) + cost[i-1],
                dfs(i-2) + cost[i-2]
            )
            return cache[i]
        return dfs(len(cost))