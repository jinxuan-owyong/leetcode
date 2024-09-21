# 452. Minimum Number of Arrows to Burst Balloons

from utils import chunk
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        curr = points[0]
        arrows = 0
        # uncomment to see the valid x-axes to shoot arrow from
        # arr = []
        for interval in points[1:]:
            if interval[0] <= curr[1]:
                # keep only overlapping intervals
                curr = [max(curr[0], interval[0]), min(curr[1], interval[1])]
            else:
                # arr.append(curr)
                curr = interval
                arrows += 1

        # add arrow required in last iteration
        return arrows + 1


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[10, 16], [2, 8], [1, 6], [7, 12]],
        [[1, 2], [3, 4], [5, 6], [7, 8]],
        [[1, 2], [2, 3], [3, 4], [4, 5]],
        [[1, 2]],
        [[1, 2], [5, 6]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findMinArrowShots(*puzzle))
