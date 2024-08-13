# 981. Time Based Key-Value Store

import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamps are strictly increasing
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        res = bisect.bisect_left(
            self.store[key], timestamp, key=lambda x: x[0])
        if res == 0 and self.store[key] and timestamp < self.store[key][0][0]:
            return ""
        if res == len(self.store[key]) or self.store[key][res][0] > timestamp:
            res -= 1
        return self.store[key][res][1]


if __name__ == "__main__":
    puzzles = [
        (["TimeMap", "set", "get", "get", "set", "get", "get"],
         [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]])
    ]
    for operations, params in puzzles:
        obj = TimeMap()
        for op, param in zip(operations[1:], params[1:]):
            print(getattr(obj, op)(*param))
        print()
