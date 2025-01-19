class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue=deque()
        queue.append(root)
        ans=[]

        while queue:
            n=len(queue)
            level=[]
            for i in range(n):
                node=queue.popleft()
                level.append(node.val)

                if node.left : queue.append(node.left)
                if node.right: queue.append(node.right)

            ans.append(level)

        return ans