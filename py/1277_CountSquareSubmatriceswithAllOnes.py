# 1277. Count Square Submatrices with All Ones

from utils import chunk
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                # a cell can form larger square(s) with its top left, right and top
                # neighbours if itself is a "1". using this recurrence relation, we
                # can use a bottom-up approach to calculate the number of squares that
                # can be formed at each cell (with the cell itself as the bottom right
                # for >2x2 squares)
                neighbours = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = neighbours + 1

        return sum([sum(row) for row in dp])


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]],
        [[1, 0, 1], [1, 1, 0], [1, 1, 0]],
        [[1]],
        [[1, 1, 1]],
        [[1], [0], [1]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countSquares(*puzzle))
