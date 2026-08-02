class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        water = 0
        while l <= r:
            if maxLeft < maxRight:
                water += max(maxLeft, height[l]) - height[l]
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                water += max(maxRight, height[r]) - height[r]
                maxRight = max(maxRight, height[r])
                r -= 1
        return water