class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair (index, height)
        for i, h in enumerate(heights):
            leftBoundry = i
            while stack and stack[-1][1] > h:
                leftBoundry, height = stack.pop()
                maxArea = max(maxArea, height * (i - leftBoundry))
            stack.append((leftBoundry, h))
        while stack:
            leftBoundry, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - leftBoundry))
        return maxArea


