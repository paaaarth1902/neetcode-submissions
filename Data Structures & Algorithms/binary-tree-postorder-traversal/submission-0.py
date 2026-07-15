# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preOrder(root):
            if root == None:
                return
            
            preOrder(root.left)
            preOrder(root.right)
            res.append(root.val)
        
        preOrder(root)

        return res