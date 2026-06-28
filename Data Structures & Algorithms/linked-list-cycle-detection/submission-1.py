# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False

        curr = head
        sl = curr
        fa = curr

        while (fa != None and fa.next != None):
            sl = sl.next
            fa = fa.next.next

            if fa == sl: return True

        return False
        