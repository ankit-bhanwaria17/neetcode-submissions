class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (leftBoundary for height, height)
        for i, currHeight in enumerate(heights):
            leftBoundary = i
            while stack and currHeight < stack[-1][1]:
                leftBoundary, height = stack.pop() # keep updating leftBoundary
                maxArea = max(maxArea, height * (i - leftBoundary))
            stack.append((leftBoundary, currHeight))
        while stack:
            leftBoundary, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - leftBoundary))
            # remaining all 'h' can be extended till the end
            # That's why its len(heights) - leftBoundary
        return maxArea