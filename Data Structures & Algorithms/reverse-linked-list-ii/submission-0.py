# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, m1, m2):
        prev = None
        curr = m1
        temp = m1
        end = m2.next

        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev, temp

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        k1 = dummy
        p1, p2 = dummy, dummy
        m1, m2 = dummy, dummy
        cnt = -1

        while k1 != None:
            cnt += 1
            if cnt == left - 1:
                p1 = k1
                m1 = p1.next
            if cnt == right:
                m2 = k1
                p2 = m2.next
            
            k1 = k1.next

        
        head1, tail1 = self.reverse(m1, m2)

        p1.next = head1
        tail1.next = p2

        return dummy.next

        
        