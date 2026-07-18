class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights)-1
        while l < r:
            water = min(heights[l], heights[r])*(r-l)
            maxWater = max(maxWater, water)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxWater