class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            best = float("inf")
            for c in coins:
                if i-c >= 0 and dp[i-c] != -1:
                    best = min(best, 1 + dp[i-c])
            if best != float("inf"):
                dp[i] = best
        return dp[amount]         