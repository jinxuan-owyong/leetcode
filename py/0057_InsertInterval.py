# 57. Insert Interval

from utils import chunk
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert until newInterval needs to be merged
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1

        res = intervals[:i]
        curr = newInterval
        # merge intervals until curr does not overlap with intervals[i]
        while i < len(intervals) and curr[1] >= intervals[i][0]:
            curr[0] = min(curr[0], intervals[i][0])
            curr[1] = max(curr[1], intervals[i][1])
            i += 1
        res.append(curr)

        # add the remaining intervals if any, they are already sorted
        res.extend(intervals[i:])
        return res


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [[1, 3], [6, 9]],
        [2, 5],
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        [4, 8],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().insert(*puzzle))
