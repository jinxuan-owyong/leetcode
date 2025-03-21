# 295. Find Median from Data Stream

import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # max heap
        self.big = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        both = self.small and self.big

        # rebalance heap value if necessary
        if both and -self.small[0] > self.big[0]:
            heapq.heappush(self.big, -heapq.heappop(self.small))

        # rebalance heap size - off by at most 1
        if len(self.small) > len(self.big) + 1:
            heapq.heappush(self.big, -heapq.heappop(self.small))
        if len(self.small) + 1 < len(self.big):
            heapq.heappush(self.small, -heapq.heappop(self.big))

    def findMedian(self) -> float:
        # invariant: abs(len(self.small) - len(self.big)) <= 1
        s, b = len(self.small), len(self.big)
        if s == b:
            # average of medians
            return (-self.small[0] + self.big[0]) / 2
        elif s > b:
            return -self.small[0]
        else:
            return self.big[0]


if __name__ == "__main__":
    puzzles = [
        (["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
         [[], [1], [2], [], [3], []])
    ]
    for words, prefixes in puzzles:
        obj = MedianFinder()
        for word, prefix in zip(words[1:], prefixes[1:]):
            print(getattr(obj, word)(*prefix))
        print()
