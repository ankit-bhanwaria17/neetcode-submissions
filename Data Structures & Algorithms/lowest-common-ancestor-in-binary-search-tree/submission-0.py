# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = root
        def dfs(curr, p, q):
            if not curr:
                return None
            if (p <= curr.val <= q) or (q <= curr.val <= p):
                self.res = curr
                return
            if curr.val > p and curr.val > q:
                dfs(curr.left, p, q)
            if curr.val < p and curr.val < q:
                dfs(curr.right, p, q)
        dfs(root, p.val, q.val)
        return self.res