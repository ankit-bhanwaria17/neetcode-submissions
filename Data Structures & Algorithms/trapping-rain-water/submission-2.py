class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeightOnRight = [0]*(len(height))
        maxHeightOnRight[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            maxHeightOnRight[i] = max(height[i], maxHeightOnRight[i+1])
        result = 0
        maxLeft = height[0]
        print(maxHeightOnRight)
        for i in range(len(height)):
            water = min(maxLeft, maxHeightOnRight[i]) - height[i]
            maxLeft = max(maxLeft, height[i])
            if water >0:
                result += water
        return result
            