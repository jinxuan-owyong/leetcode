# 3394. Check if Grid can be Cut into Sections

from utils import chunk
from typing import List, Callable


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        """
        we can only make 2 horizontal or vertical cuts
        merging the intervals separately for x and y allows to identify the non-overlapping regions of all rectangles,
        which will give us at least a full rectangle after cutting 
        using the x-intervals and y-intervals, if there are at least 3 intervals in either, then there is a valid cut
        """
        def getXValues(rect: List[int]) -> List[int]:
            return [rect[0], rect[2]]

        def getYValues(rect: List[int]) -> List[int]:
            return [rect[1], rect[3]]

        # instead of merging the full set of values, we can prune execution if len >= 3 here as well
        def merge(getter: Callable[[int], List[int]]) -> List[List[int]]:
            intervals = []
            prev = getter(rectangles[0])
            for i in range(1, len(rectangles)):
                curr = getter(rectangles[i])
                if prev[1] > curr[0]:
                    prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                else:
                    intervals.append(prev)
                    prev = curr
            intervals.append(prev)
            return intervals

        rectangles.sort(key=getXValues)
        xIntervals = merge(getXValues)

        rectangles.sort(key=getYValues)
        yIntervals = merge(getYValues)

        return len(xIntervals) >= 3 or len(yIntervals) >= 3


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        5,
        [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]],
        4,
        [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]],
        4,
        [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().checkValidCuts(*puzzle))
