class Solution:
    def trap(self, height: List[int]) -> int:
        l ,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        water = 0
        while l <= r:
            if leftMax < rightMax:
                leftMax = max(leftMax, height[l])
                water += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]
                r -= 1
        return water