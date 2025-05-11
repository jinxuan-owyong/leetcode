# 3546. Equal Sum Grid Partition I

from utils import chunk
from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        rowSum = [0] * ROWS
        colSum = [0] * COLS
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                rowSum[i] += c
                colSum[j] += c
        total = sum(rowSum)

        # check for horizontal cuts
        top = rowSum[0]
        bot = total - rowSum[0]
        i = 1
        while i < ROWS:
            if top == bot:
                return True
            top += rowSum[i]
            bot -= rowSum[i]
            i += 1

        # check for vertical cuts
        left = colSum[0]
        right = total - colSum[0]
        j = 1
        while j < COLS:
            if left == right:
                return True
            left += colSum[j]
            right -= colSum[j]
            j += 1

        return False


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 4], [2, 3]],
        [[1, 3], [2, 4]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().canPartitionGrid(*puzzle))
