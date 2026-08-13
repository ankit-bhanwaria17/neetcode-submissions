class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        cache = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            cache[i][0] = 1
        
        for i in range(n-1, -1, -1):
            for a in range(amount+1):
                if a >= coins[i]:
                    cache[i][a] = cache[i+1][a]
                    cache[i][a] += cache[i][a - coins[i]]
        return cache[0][amount]