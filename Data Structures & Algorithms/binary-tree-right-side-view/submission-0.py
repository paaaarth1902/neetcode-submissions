class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if i == l - 1:
                    res.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        
        return res