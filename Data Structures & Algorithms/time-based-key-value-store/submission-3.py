class TimeMap:

    def __init__(self):
        self.store = {} # key: [[timestamp, value], [] ....]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or self.store[key][0][0] > timestamp:
            return ""
        l, r = 0, len(self.store[key])-1
        if self.store[key][r][0] <= timestamp:
            return self.store[key][r][1]
        res = ""
        print(self.store)
        print(timestamp)
        while l <= r:
            mid = l + (r-l)//2
            if self.store[key][mid][0] == timestamp:
                return self.store[key][mid][1]

            if timestamp < self.store[key][mid][0]:
                r = mid-1
            else:
                res = self.store[key][mid][1]
                l = mid+1
        return res
