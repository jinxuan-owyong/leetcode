# 3169. Count Days Without Meetings

from utils import chunk
from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        # merge overlapping intervals
        prev = meetings[0]
        merged = []
        for i in range(1, len(meetings)):
            curr = meetings[i]
            if prev[1] >= curr[0]:
                prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
            else:
                merged.append(prev)
                prev = curr
        merged.append(prev)

        # count days without meetings
        without = 0
        start = 1
        for meet in merged:
            without += meet[0] - start
            start = meet[1] + 1

        # if the last meeting is not on the last day
        if merged and merged[-1][1] < days:
            without += days - merged[-1][1]

        return without


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        10,
        [[5, 7], [1, 3], [9, 10]],
        5,
        [[2, 4], [1, 3]],
        6,
        [[1, 6]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countDays(*puzzle))
