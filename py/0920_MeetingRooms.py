# 920. Meeting Rooms

from utils import chunk
from typing import List
from lintcode import Interval


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))
        
        for i in range(1, len(intervals)):
            prev, curr = intervals[i - 1], intervals[i]
            if prev.end > curr.start:
                return False
        
        return True

if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [(0, 30), (5, 10), (15, 20)],
        [(5, 8), (9, 15)]
    ]
    for puzzle in chunk(puzzles, testSize):
        puzzle = list(map(lambda x: Interval(*x), puzzle[0]))
        print(Solution().canAttendMeetings(puzzle))
