# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev=[None]
        balanced=[True]
        def dfs(node):
            if not node or not balanced[0]:
                return
            dfs(node.left)
            if prev[0] is not None and prev[0]>=node.val:
                balanced[0]=False
                return
            prev[0]=node.val
            dfs(node.right)
        dfs(root)
        return balanced[0]