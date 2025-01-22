# 1765. Map of Highest Peak

from utils import chunk
from typing import List
from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """
        since all water cells have height 0, we treat them as starting points for level-order BFS
        the first cell visited from a water cell is height 1, then 2, 3, ...
        """
        ROWS, COLS = len(isWater), len(isWater[0])
        queue = deque()
        visited = [[False] * COLS for _ in range(ROWS)]
        for i, row in enumerate(isWater):
            for j, cell in enumerate(row):
                if cell:
                    queue.append((i, j))
                    visited[i][j] = True

        height = [[0] * COLS for _ in range(ROWS)]
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    y, x = i + dy, j + dx
                    if y in range(ROWS) and x in range(COLS) and not isWater[y][x]:
                        if not visited[y][x]:
                            visited[y][x] = True
                            height[y][x] = height[i][j] + 1
                            queue.append((y, x))
        return height


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[0, 1], [0, 0]],
        [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().highestPeak(*puzzle))
