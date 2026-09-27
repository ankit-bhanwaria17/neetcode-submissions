# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(node):
            """
            dfs returns the best path that can continue through the node's parent, 
            so it can use only one child. res also considers paths that use both children.
            """
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            nonlocal res
            res = max(
                res, 
                leftMax + rightMax + node.val
            )
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res