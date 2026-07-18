class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largestPile = max(piles)
        left, right = 1, largestPile
        result = 1
        while left <= right:
            k = left + (right - left)//2
            timeTaken = 0
            for p in piles:
                timeTaken += math.ceil(p/k)
            if timeTaken <= h:
                right = k - 1
                result = k
            else:
                left = k + 1
        return result
