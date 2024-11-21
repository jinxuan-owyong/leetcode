# 2257. Count Unguarded Cells in the Grid

from utils import chunk
from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # x = unguarded, w = wall, G = guard, g = guarded cell
        cells = [['x'] * n for _ in range(m)]

        guarded = 0

        def guard(i, j, c):
            nonlocal guarded
            if cells[i][j] in 'gG':
                return
            cells[i][j] = c
            guarded += 1

        for row, col in walls:
            cells[row][col] = 'w'

        for row, col in guards:
            guard(row, col, 'G')

        for row, col in guards:
            for j in reversed(range(0, col)):
                if cells[row][j] in 'wG':
                    break
                guard(row, j, 'g')
            for j in range(col + 1, n):
                if cells[row][j] in 'wG':
                    break
                guard(row, j, 'g')
            for i in reversed(range(0, row)):
                if cells[i][col] in 'wG':
                    break
                guard(i, col, 'g')
            for i in range(row + 1, m):
                if cells[i][col] in 'wG':
                    break
                guard(i, col, 'g')

        return m * n - guarded - len(walls)


if __name__ == "__main__":
    testSize = 4
    puzzles = [
        4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]],
        3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countUnguarded(*puzzle))

# TLE
# class Solution:
#     def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
#         # keep track of walls that exist per row/col
#         wallCol = [list() for row in range(m)]
#         wallRow = [list() for col in range(n)]
#         for row, col in walls:
#             bisect.insort(wallCol[row], col)
#             bisect.insort(wallRow[col], row)

#         guarded = [[0] * n for _ in range(m)]
#         for row, col in guards:
#             # G
#             if len(wallCol[row]) == 0:
#                 start, end = 0, n
#             # GW
#             elif col < wallCol[row][0]:
#                 start, end = 0, wallCol[row][0]
#             # WG
#             elif wallCol[row][-1] < col:
#                 start, end = wallCol[row][-1] + 1, n
#             # WGW
#             else:
#                 i = bisect.bisect_left(wallCol[row], col)
#                 if col < wallCol[row][i]:
#                     i -= 1
#                 start, end = wallCol[row][i] + 1, wallCol[row][i + 1]

#             for i in range(start, end):
#                 guarded[row][i] = 1

#              # G
#             if len(wallRow[col]) == 0:
#                 start, end = 0, m
#             # GW
#             elif row < wallRow[col][0]:
#                 start, end = 0, wallRow[col][0]
#             # WG
#             elif wallRow[col][-1] < row:
#                 start, end = wallRow[col][-1] + 1, m
#             # WGW
#             else:
#                 i = bisect.bisect_left(wallRow[col], row)
#                 if row < wallRow[col][i]:
#                     i -= 1
#                 start, end = wallRow[col][i] + 1, wallRow[col][i + 1]

#             for i in range(start, end):
#                 guarded[i][col] = 1

#         return m * n - sum(map(sum, guarded)) - len(walls)
