class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        def height(root):
            if root is None:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            self.max_d = max(self.max_d, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        height(root)

        return self.max_d


        