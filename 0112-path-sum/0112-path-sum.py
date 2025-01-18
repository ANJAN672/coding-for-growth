# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def root_to_leaf(root,summ):
            if not root:
                return False
            summ+=root.val
            if not root.left and not root.right:
                return summ==targetSum
            return root_to_leaf(root.left,summ) or root_to_leaf(root.right,summ)
        return root_to_leaf(root,0)