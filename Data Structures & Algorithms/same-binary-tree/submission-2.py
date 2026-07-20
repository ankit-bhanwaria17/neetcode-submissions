# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        if (not p and q) or (p and not q):
            return False
        def dfs(r1, r2):
            if (not r1 and r2) or (r1 and not r2):
                return False
            if not r1 and not r2:
                return True
            if r1.val != r2.val:
                return False
            nonlocal res
            localres = dfs(r1.left, r2.left) and dfs(r1.right, r2.right) 
            res = res and localres
            return localres
        res = dfs(p, q)
        return res