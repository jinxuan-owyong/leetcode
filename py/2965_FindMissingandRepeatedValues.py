# 2965. Find Missing and Repeated Values

from utils import chunk
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # 2 <= n <= 50
        N = len(grid)
        count = [0] * (N*N + 1)
        for row in grid:
            for el in row:
                count[el] += 1

        result = [0, 0]
        for i, freq in enumerate(count):
            if freq == 2:
                result[0] = i
            if freq == 0:
                result[1] = i

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 3], [2, 2]],
        [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findMissingAndRepeatedValues(*puzzle))
