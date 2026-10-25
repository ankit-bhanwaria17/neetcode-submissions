class Solution:
    def trap(self, height: List[int]) -> int:
        maxRightHeight = [0]*(len(height))
        maxHeight = height[len(height)-1]
        for i in range(len(height)-1, -1, -1):
            maxHeight = max(maxHeight, height[i])
            maxRightHeight[i] = maxHeight
        water = 0
        maxHeight = height[0]
        for i in range(len(height)):
            maxHeight = max(maxHeight, height[i])
            water += min(maxHeight, maxRightHeight[i]) - height[i]
        return water