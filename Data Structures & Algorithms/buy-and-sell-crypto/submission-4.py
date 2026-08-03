class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minSoFar = prices[0]
        i = 0
        for i in range(len(prices)):
            minSoFar = min(minSoFar, prices[i])
            profit = max(profit, prices[i] - minSoFar)
        return profit