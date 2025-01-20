# 2661. First Completely Painted Row or Column

from utils import chunk
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # keep track of number of unpainted cells remaining
        row = [len(mat[0])] * len(mat)
        col = [len(mat)] * len(mat[0])

        # store the integer positions for fast lookup
        pos = {}
        for i, r in enumerate(mat):
            for j, el in enumerate(r):
                pos[el] = (i, j)

        for k, el in enumerate(arr):
            i, j = pos[el]
            # ensure that the row/col decrement is only counted once with mat[i][j] = -1
            if mat[i][j] >= 0:
                mat[i][j] = -1
                row[i] -= 1
                col[j] -= 1
                if row[i] == 0 or col[j] == 0:
                    return k


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 3, 4, 2], [[1, 4], [2, 3]],
        [2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().firstCompleteIndex(*puzzle))
