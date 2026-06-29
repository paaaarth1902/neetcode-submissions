# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hm = {}
        p1, p2 = headA, headB

        while p1 != None:
            if p1 not in hm:
                hm[p1] = True
            p1 = p1.next

        while p2 != None:
            if p2 in hm:
                return p2
            p2 = p2.next

        
        return None
        