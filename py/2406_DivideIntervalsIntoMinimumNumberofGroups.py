# 2406. Divide Intervals Into Minimum Number of Groups

from utils import chunk
from typing import List
import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        # the maximum size of currnt at a given time tells us how many
        # overlapping intervals are present. the maximum overlaps + 1
        # tells us how many groups are required to divide the intervals
        current = []
        overlap = 0
        for left, right in intervals:
            # we pop the intervals until currRight > newLeft
            # strict inequality since we want disjoint intervals
            while current and current[0] < left:
                heapq.heappop(current)

            overlap = max(len(current), overlap)
            heapq.heappush(current, right)

        return overlap + 1


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]],
        [[1, 3], [5, 6], [8, 10], [11, 13]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minGroups(*puzzle))
