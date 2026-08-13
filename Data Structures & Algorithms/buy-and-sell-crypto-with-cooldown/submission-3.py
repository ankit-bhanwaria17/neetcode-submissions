class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for canBuy in [True, False]:
                if canBuy:
                    buy = dp[i+1][False] - prices[i] if i+1<n else -prices[i]
                    notBuy = dp[i+1][True] if i+1<n else 0
                    dp[i][1] = max(buy, notBuy)
                else:
                    sell = dp[i+2][True] + prices[i] if i+2<n else prices[i]
                    notSell = dp[i+1][False] if i+1<n else 0
                    dp[i][0] = max(sell, notSell)
        return dp[0][1]