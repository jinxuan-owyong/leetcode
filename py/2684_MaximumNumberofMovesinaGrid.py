# 2684. Maximum Number of Moves in a Grid

from utils import chunk
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = {}

        def dfs(i: int, j: int, moves: int, prev: int):
            if i not in range(ROWS) or j not in range(COLS) or prev >= grid[i][j]:
                return moves - 1
            if (i, j) in cache:
                return cache[(i, j)]

            curr = grid[i][j]
            # the value of the cell you move to should be strictly bigger than the value of the current cell
            top = dfs(i - 1, j + 1, moves + 1, curr)
            right = dfs(i, j + 1, moves + 1, curr)
            bottom = dfs(i + 1, j + 1, moves + 1, curr)

            # we can memoise this value for future traversals that end up in the same cell
            cache[(i, j)] = max(top, right, bottom)
            return cache[(i, j)]

        result = 0
        # You can start at any cell in the first column of the matrix
        for i in range(ROWS):
            result = max(dfs(i, 0, 0, 0), result)
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]],
        [[3, 2, 4], [2, 1, 9], [1, 1, 7]],
        [[1]],
        [[1, 2, 3]],
        [[1], [2], [3]],
        [[3, 2, 1]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxMoves(*puzzle))
