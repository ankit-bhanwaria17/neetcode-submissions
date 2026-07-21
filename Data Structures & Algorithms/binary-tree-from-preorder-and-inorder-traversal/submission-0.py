# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cache = {}
        for i in range(len(inorder)):
            cache[inorder[i]] = i

        def dfs(l, r, i):
            if l > r or i > len(preorder)-1:
                return None
            root = preorder[i]
            mid = cache[root]
            node = TreeNode(root)
            node.left = dfs(l, mid-1, i+1)
            node.right = dfs(mid + 1, r, i + mid - l + 1)
            return node

        return dfs(0, len(inorder)-1, 0)

