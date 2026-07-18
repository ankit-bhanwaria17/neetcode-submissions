class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxWater = 0
        while l < r:
            if heights[l] < heights[r]:
                water = (r - l)*(heights[l])
                l += 1
                while l < r and heights[l] < heights[l-1]:
                    l += 1
            else:
                water = (r - l)*(heights[r])
                r -= 1
                while l < r and heights[r] < heights[r+1]:
                    r -= 1
            maxWater = max(maxWater, water)
        return maxWater