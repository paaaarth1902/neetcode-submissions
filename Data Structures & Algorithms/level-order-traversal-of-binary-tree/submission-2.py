# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            list1 = []
            len1 = len(q)
            for i in range(len1):
                n = q.popleft()
                if n:
                    list1.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if list1:
                res.append(list1)
        
        return res

            


        