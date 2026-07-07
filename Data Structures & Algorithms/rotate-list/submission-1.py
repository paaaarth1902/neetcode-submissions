# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        cnt = 0
        curr = head

        while curr:
            curr = curr.next
            cnt += 1
        
        k = k % cnt
        if k == 0:
            return head
        hops = cnt - k - 1

        c1 = 0
        p1 = head

        while c1 < hops:
            p1 = p1.next
            c1+= 1

        temp = p1.next
        t1 = temp
        p1.next = None

        while t1.next:
            t1 = t1.next
        
        t1.next = head
        return temp