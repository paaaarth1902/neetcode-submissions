class HitCounter:
    
    def __init__(self):
        self.hitArray = []

    def hit(self, timestamp: int) -> None:
        self.hitArray.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        count = 0
        for ts in self.hitArray:
            if ts > timestamp - 300:
                count += 1
        return count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
