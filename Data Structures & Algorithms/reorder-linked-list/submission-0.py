# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_middle(self, head):
        curr = head
        p1 = curr
        p2 = curr.next

        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next
        
        return p1

    def reverse_list(self, head):
        prev = None
        curr = head

        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.find_middle(head)
        rev = self.reverse_list(mid.next)

        mid.next = None

        # 0 - 1 - 2 - 3
        # 6 - 5 - 4

        p1 = head
        p2 = rev

        while p2 != None:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p2 = temp2
            p1 = temp1