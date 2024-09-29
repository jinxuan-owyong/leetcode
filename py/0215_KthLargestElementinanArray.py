# 215. Kth Largest Element in an Array

from utils import chunk
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [3, 2, 1, 5, 6, 4],
        2,
        [3, 2, 3, 1, 2, 4, 5, 5, 6],
        4
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findKthLargest(*puzzle))
