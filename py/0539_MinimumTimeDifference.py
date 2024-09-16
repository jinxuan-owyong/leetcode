# 539. Minimum Time Difference

from utils import chunk
from typing import Tuple, List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def toHHMM(time: str) -> Tuple[int]:
            t = time.split(":")
            return (int(t[0]), int(t[1]))

        def order(x: Tuple[int]) -> int:
            return x[0] * 60 + x[1]

        # can also choose to include toHHMM in order
        timePoints = list(map(toHHMM, timePoints))
        timePoints.sort(key=order)

        # check for "next" day timings
        hh, mm = timePoints[0]
        timePoints.append((hh + 24, mm))

        result = float('inf')
        for i in range(1, len(timePoints)):
            diff = order(timePoints[i]) - order(timePoints[i - 1])
            result = min(diff, result)

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["23:59", "00:00"],
        ["00:00", "23:59", "00:00"],
        ["11:59", "00:01", "23:59", "23:55"],
        ["11:59", "01:01", "23:59", "20:55"],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findMinDifference(*puzzle))
