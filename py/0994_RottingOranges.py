# 994. Rotting Oranges

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()  # i, j, minute
        totalOranges = 0

        for i, row in enumerate(grid):
            for j, orange in enumerate(row):
                if orange != EMPTY:
                    totalOranges += 1
                if orange == ROTTEN:
                    queue.append((i, j, 0))

        time = 0
        visited = set()
        rotted = 0
        while queue:
            i, j, currTime = queue.popleft()
            time = max(time, currTime)
            grid[i][j] = ROTTEN
            rotted += 1

            for dy, dx in DIRS:
                y, x = i + dy, j + dx
                if y in range(ROWS) and \
                    x in range(COLS) and \
                    (y, x) not in visited and \
                        grid[y][x] == FRESH:
                    queue.append((y, x, currTime + 1))
                    visited.add((y, x))

        return time if rotted == totalOranges else -1


if __name__ == "__main__":
    puzzles = [
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
        [[0, 2]],
        [[0]]
    ]
    for puzzle in puzzles:
        print(Solution().orangesRotting(puzzle))
