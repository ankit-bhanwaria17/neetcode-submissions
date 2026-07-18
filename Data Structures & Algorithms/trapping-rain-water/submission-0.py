class Solution:
    def trap(self, height: List[int]) -> int:
        res = []
        maxLeft = 0
        for n in height:
            maxLeft = max(maxLeft, n)
            res.append(maxLeft)
        maxRight = 0
        water = 0
        for i in range(len(height)-1, -1, -1):
            maxRight = max(maxRight, height[i])
            water = water + min(maxRight, res[i])-height[i]
        return water


