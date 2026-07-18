class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        water = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
        return water
