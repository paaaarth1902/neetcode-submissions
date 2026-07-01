# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = dummy
        cnt = 0

        while p1.next != None:
            if cnt < n:
                cnt += 1
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next

        p2.next = p2.next.next

        return dummy.next
        
        