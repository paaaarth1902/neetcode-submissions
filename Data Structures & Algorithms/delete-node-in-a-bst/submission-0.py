class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            succ = self.getMin(root.right)

            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)

        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node