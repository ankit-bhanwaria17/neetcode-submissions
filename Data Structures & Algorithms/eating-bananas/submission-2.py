class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = max(piles)
        minSpeed = 1
        res = 1
        while minSpeed <= maxSpeed:
            midSpeed = minSpeed + (maxSpeed - minSpeed) // 2
            if self.canFinishPile(piles, midSpeed, h):
                res = midSpeed
                maxSpeed = midSpeed - 1
            else:
                minSpeed = midSpeed + 1
        return res

    def canFinishPile(self, piles, speed, h):
        timeTaken = 0
        for b in piles:
            timeTaken += math.ceil(b/speed)
            if timeTaken > h:
                return False
        return True
        