# 48. Rotate Image

from utils import chunk
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # rotate = transpose + flip along vertical axis OR
        #          flip along horizontal axis + transpose (easier)

        i, j = 0, len(matrix)-1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    ]
    for puzzle in chunk(puzzles, testSize):
        Solution().rotate(*puzzle)
        for row in puzzle[0]:
            print(row)
        print()
