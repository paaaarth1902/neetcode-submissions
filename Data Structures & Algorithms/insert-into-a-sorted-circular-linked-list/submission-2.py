# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if not head:
            head = newNode
            head.next = newNode
            return head
        
        prev = head
        curr = head.next

        while True:
            if (prev.val <= insertVal <= curr.val) or (prev.val > curr.val and insertVal >= prev.val) or (prev.val > curr.val and insertVal <= curr.val):
                prev.next = newNode
                newNode.next = curr
                break
            
            prev = prev.next
            curr = curr.next
    
            if prev == head: 
                prev.next = newNode
                newNode.next = curr
                break

        return head