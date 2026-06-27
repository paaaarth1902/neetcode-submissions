# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        p1 = curr
        p2 = curr

        while (p2 != None and p2.next != None):
            p1 = p1.next
            p2 = p2.next.next

        head = p1

        return p1
        