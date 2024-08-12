# 703. Kth Largest Element in a Stream

from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    puzzles = [
        (["KthLargest", "add", "add", "add", "add", "add"],
         [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]])
    ]
    for operations, arguments in puzzles:
        obj = KthLargest(*arguments[0])
        for op, arg in zip(operations[1:], arguments[1:]):
            method = getattr(obj, op)
            if not arg:
                print(method())
            else:
                print(method(arg[0]))
