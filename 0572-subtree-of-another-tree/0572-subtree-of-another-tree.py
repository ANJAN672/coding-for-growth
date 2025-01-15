# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            return (
                root.val == subRoot.val and
                isSame(root.left, subRoot.left) and
                isSame(root.right, subRoot.right)
            )

        if not subRoot:
            return True
        if not root:
            return False
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
