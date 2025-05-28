# 253. Meeting Rooms II

from utils import chunk
from classes import Interval
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # to successfully schedule all meetings, we need to count what is the maximum number of overlapping meetings at a given time
        # by simulating the current time, we can keep track of the current ongoing meetings using sorted start and end times
        start = sorted(map(lambda x: x.start, intervals))
        end = sorted(map(lambda x: x.end, intervals))

        # current time is start[i]
        i, j = 0, 0
        currRooms = 0
        maxRooms = 0

        while i < len(start):
            while j < len(end) and end[j] <= start[i]:
                currRooms -= 1
                j += 1
            currRooms += 1
            if currRooms > maxRooms:
                maxRooms = currRooms
            i += 1

        return maxRooms


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [(0, 40), (5, 10), (15, 20)],
        [(4, 9)],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minMeetingRooms(
            list(map(lambda x: Interval(start=x[0], end=x[1]), puzzle[0]))))
