class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root

        lefft = self.lowestCommonAncestor(root.left, p, q)
        righht = self.lowestCommonAncestor(root.right, p, q)

        if lefft and righht:
            return root

        return lefft or righht