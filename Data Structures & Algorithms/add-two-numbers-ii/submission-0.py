# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, l):
        prev = None
        curr = l

        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def addTwoNumbersReversed(self, l1, l2):
        p1 = l1
        p2 = l2

        dummy = ListNode()
        curr = dummy
        carry = 0

        while p1 or p2 or carry != 0:
            if p1 and not p2:
                s = p1.val + carry
            elif p2 and not p1:
                s = p2.val + carry
            elif p1 and p2:
                s = p1.val + p2.val + carry
            else:
                s = carry
                
            carry = s // 10
            s = s % 10
            newNode = ListNode(s)
            curr.next = newNode
            curr = newNode

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        return dummy.next
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Rev = self.reverse(l1)
        l2Rev = self.reverse(l2)

        reversedOP = self.addTwoNumbersReversed(l1Rev, l2Rev)

        return self.reverse(reversedOP)
        