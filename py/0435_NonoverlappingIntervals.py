# 435. Non-overlapping Intervals

from utils import chunk
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # remove larger intervals first
        intervals.sort()

        invalid = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]

            # not overlapping
            if prev[1] <= curr[0]:
                prev = curr
            else:
                invalid += 1
                # decide which one to remove
                # we "discard" prev if its end value is larger
                if curr[1] < prev[1]:
                    prev = curr

        return invalid


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 2], [2, 3], [3, 4], [1, 3]],
        [[1, 2], [1, 2], [1, 2]],
        [[1, 2], [2, 3]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().eraseOverlapIntervals(*puzzle))
