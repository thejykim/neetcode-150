from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.table[key]

        lo, hi = 0, len(vals) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif vals[mid][0] < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1
        
        if hi >= 0:
            return vals[hi][1]
        else:
            return ""
