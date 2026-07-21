# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(curr, a, b):
            if not curr:
                return True
            if not (a < curr.val < b):
                return False
            return validate(curr.left, a, curr.val) and validate(curr.right, curr.val, b)
        return validate(root, float('-inf'), float('inf'))
        