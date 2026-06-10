class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
       
        n = len(self.timeMap[key])
        start = 0
        end = n - 1
        res = (0, "")

        while start <= end:
            mid = start + (end - start) // 2


            if self.timeMap[key][mid][0] <  timestamp:
                res = self.timeMap[key][mid]
                start = mid + 1
            elif self.timeMap[key][mid][0] > timestamp:
                end = mid - 1
            else:
                return self.timeMap[key][mid][1]
        
        return res[1]
                
        
