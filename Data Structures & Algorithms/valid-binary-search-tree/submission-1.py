# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.inorder.append(root.val)
            dfs(root.right)
        dfs(root)
        for i in range(1, len(self.inorder)):
            if self.inorder[i-1] >= self.inorder[i]:
                return False
        return True
