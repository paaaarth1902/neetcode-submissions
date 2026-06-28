# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# BF: using Hashmap
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm = {}
        curr = head

        while curr != None:
            if curr not in hm:
                hm[curr] = True
                curr = curr.next
            else:
                return True

        return False