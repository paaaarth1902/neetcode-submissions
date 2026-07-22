class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val > q.val or q.val > root.val > p.val:
            return root
        
        if root.val == p.val or root.val == q.val:
            return root
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return self.lowestCommonAncestor(root.left, p, q)