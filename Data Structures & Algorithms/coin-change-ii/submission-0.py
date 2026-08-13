class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {} # key: (i, total) value: ways
        def dfs(i, total):
            if total > amount or i >= len(coins):
                return 0
            if total == amount:
                return 1
            if (i, total) in cache:
                return cache[(i, total)]

            skipCoin = dfs(i+1, total)
            useCoin = dfs(i, total+coins[i])

            cache[(i, total)] = skipCoin + useCoin
            return cache[(i, total)]

        return dfs(0, 0)