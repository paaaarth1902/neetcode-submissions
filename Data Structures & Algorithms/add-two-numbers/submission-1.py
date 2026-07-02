class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy

        p1, p2, carry = l1, l2, 0

        while p1 != None or p2 != None or carry != 0:
            if p1 != None:
                v1 = p1.val
            else:
                v1 = 0
            if p2 != None:
                v2 = p2.val
            else:
                v2 = 0

            s = v1 + v2 + carry
            newNode = ListNode(s % 10)
            carry = s // 10

            temp.next = newNode
            temp = newNode

            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next

        return dummy.next

            

        