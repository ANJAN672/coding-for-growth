# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca=[root]
        def search(root):
            lca[0]=root

            if not root:
                return
            if root.val>p.val and root.val>q.val:
                search(root.left)
            elif root.val<p.val and root.val<q.val:
                search(root.right)
            else:
                return
        search(root)
        return lca[0]