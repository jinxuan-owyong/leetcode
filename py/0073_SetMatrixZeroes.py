# 73. Set Matrix Zeroes

from utils import chunk
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        # use separate flags for the first row/col because they cannot be used to identify themselves
        firstRowZero = False
        firstColZero = False

        # set the whole row/col to zero as long as there is one zero
        # mark whether a row/col contains a zero using the 0th-index
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    firstRowZero = i == 0 or firstRowZero
                    firstColZero = j == 0 or firstColZero
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # replace the first row/col last to prevent overwriting the zero flags
        # alternatively: loop through all m*n cells and set to 0 if matrix[i][0] == 0 or matrix[0][j] == 0
        for i in range(1, ROWS):
            if matrix[i][0] == 0:
                for j in range(1, COLS):
                    matrix[i][j] = 0

        for j in range(1, COLS):
            if matrix[0][j] == 0:
                for i in range(1, ROWS):
                    matrix[i][j] = 0

        if firstRowZero:
            for j in range(COLS):
                matrix[0][j] = 0

        if firstColZero:
            for i in range(ROWS):
                matrix[i][0] = 0


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    ]
    for puzzle in chunk(puzzles, testSize):
        Solution().setZeroes(*puzzle)
        for row in puzzle[0]:
            print(row)
        print()
