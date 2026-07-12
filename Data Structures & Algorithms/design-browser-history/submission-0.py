class Node:
    def __init__(self, val:str, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.temp = self.head
        self.cnt = 0

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.temp.next = newNode
        newNode.prev = self.temp
        newNode.next = None
        self.temp = self.temp.next
        self.cnt += 1

    def back(self, steps: int) -> str:
        while steps > 0 and self.temp.prev != None:
            self.temp = self.temp.prev
            steps -= 1
        return self.temp.val

    def forward(self, steps: int) -> str:
        while self.temp.next != None and steps > 0:
            self.temp = self.temp.next
            steps -= 1
        return self.temp.val

