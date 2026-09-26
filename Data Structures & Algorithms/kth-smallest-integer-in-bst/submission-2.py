# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = root.val
        self.count = k
        def dfs(curr):
            if not curr:
                return
            dfs(curr.left)
            if self.count == 0:
                return
            self.count -= 1
            if self.count == 0:
                self.result = curr.val
                return
            dfs(curr.right)
        dfs(root)
        return self.result