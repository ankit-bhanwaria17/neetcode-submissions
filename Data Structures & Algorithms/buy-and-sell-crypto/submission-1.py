class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            while prices[l] > prices[r] and l < r:
                l += 1
            maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        return maxProfit