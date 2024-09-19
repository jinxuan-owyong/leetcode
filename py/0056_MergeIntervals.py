# 56. Merge Intervals

from utils import chunk
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the inputs in non-decreasing order
        intervals.sort()

        result = []
        curr = intervals[0]
        for interval in intervals[1:]:
            a1, b1 = curr
            a2, b2 = interval
            # merge if overlapping
            # a1 >= b2 is not possible
            # suppose b2 is 2 and a1 is 3, then a2 <= 2
            # not possible for a2 to come after a1 since sorted
            if a2 <= b1:
                curr = [min(a1, a2), max(b1, b2)]
            else:
                result.append(curr)
                curr = interval

        result.append(curr)
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[3, 5], [3, 4], [1, 4], [2, 3], [1, 2]],
        [[3, 8]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().merge(*puzzle))
