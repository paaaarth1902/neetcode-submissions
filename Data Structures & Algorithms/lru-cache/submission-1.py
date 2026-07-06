class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cacheMap = {}
        self.size = capacity
        self.left, self.right = Node(0, 0), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left
        
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
            self.insert(self.cacheMap[key])
            return self.cacheMap[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
        newNode = Node(key, value)
        self.cacheMap[key] = newNode
        self.insert(newNode)

        if len(self.cacheMap) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cacheMap[lru.key]
        
