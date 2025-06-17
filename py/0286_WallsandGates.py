# 286. Walls and Gates

from utils import chunk
from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER = -1
        TREASURE = 0

        def findStart():
            result = []
            for i, row in enumerate(grid):
                for j, cell in enumerate(row):
                    if cell == TREASURE:
                        result.append([i, j])
            return result

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque(findStart())
        dist = 0
        visited = [[False] * COLS for _ in range(ROWS)]
        while queue:
            # perform level-order traversal of the grid
            # the first frontier to reach a cell is always the smallest,
            # since we update the cells starting from the smallest distance
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i not in range(ROWS) or \
                        j not in range(COLS) or \
                        visited[i][j] or \
                        grid[i][j] == WATER:
                    continue
                visited[i][j] = True
                grid[i][j] = min(grid[i][j], dist)
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    queue.append((i+dy, j+dx))
            dist += 1


if __name__ == "__main__":
    INF = 2147483647
    testSize = 1
    puzzles = [
        [[INF, -1, 0, INF],
         [INF, INF, INF, -1],
         [INF, -1, INF, -1],
         [0, -1, INF, INF]],
        [[0, -1],
         [INF, INF]],
    ]
    for puzzle in chunk(puzzles, testSize):
        Solution().islandsAndTreasure(*puzzle)
        print(puzzle[0])
