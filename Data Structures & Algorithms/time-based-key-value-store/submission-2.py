class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        self.hm[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""

        l = 0
        h = len(self.hm[key]) - 1
        res = ("", 0)

        while l <= h:
            m = l + (h - l) // 2

            if self.hm[key][m][1] < timestamp:
                res = self.hm[key][m]
                l = m + 1
            elif self.hm[key][m][1] > timestamp:
                h = m - 1
            else:
                return self.hm[key][m][0]

        return res[0]