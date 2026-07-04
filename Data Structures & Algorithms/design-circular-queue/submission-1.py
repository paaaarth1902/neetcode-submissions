class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.head = Node(0)
        self.tail = Node(-1)
        self.cnt = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            newNode = Node(value)
            self.head = newNode
            newNode.prev = None
            self.tail = newNode

        elif self.isFull():
            return False
        else:
            newNode = Node(value)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
        self.cnt += 1
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            newHead = self.head.next
            self.head = newHead
            self.cnt -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.cnt == 0
        
    def isFull(self) -> bool:
        return self.cnt == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()