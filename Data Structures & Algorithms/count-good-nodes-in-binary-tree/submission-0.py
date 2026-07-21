# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(curr, maxVal):
            if not curr:
                return
            currMax = maxVal
            if curr.val >= maxVal:
                self.count += 1
                currMax = curr.val
            dfs(curr.left, currMax)
            dfs(curr.right, currMax)
        dfs(root, float('-inf'))
        return self.count