# 1091. Shortest Path in Binary Matrix


from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1))

        queue = deque()
        queue.append((0, 0, 1))
        visited = set()
        visited.add((0, 0))

        while queue:
            i, j, cost = queue.popleft()
            if i == ROWS - 1 and j == COLS - 1 and grid[i][j] == 0:
                return cost

            for dy, dx in DIRS:
                y, x = i + dy, j + dx
                isWithinGrid = y in range(ROWS) and x in range(COLS)
                isVisited = (y, x) in visited
                if isVisited or not isWithinGrid:
                    continue
                if grid[y][x] == 0:
                    queue.append((y, x, cost + 1))
                    visited.add((y, x))

        return -1


if __name__ == "__main__":
    puzzles = [
        [[0, 1], [1, 0]],
        [[0, 0, 0], [1, 1, 0], [1, 1, 0]],
        [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    ]
    for puzzle in puzzles:
        print(Solution().shortestPathBinaryMatrix(puzzle))
