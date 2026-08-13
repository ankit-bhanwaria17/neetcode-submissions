class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}  # key (i, canBuy): profit

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in cache:
                return cache[(i, canBuy)]
            if canBuy:
                # buy today, or skip today
                profit = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
            else:
                # sell today (then cooldown), or keep holding
                profit = max(dfs(i + 2, True) + prices[i], dfs(i + 1, False))
            cache[(i, canBuy)] = profit
            return profit

        return dfs(0, True)