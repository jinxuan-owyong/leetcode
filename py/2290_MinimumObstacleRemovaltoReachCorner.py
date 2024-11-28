# 2290. Minimum Obstacle Removal to Reach Corner

from utils import chunk
from typing import List
import heapq


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # treat empty -> walls as paths with edge weight 1
        # using a priority queue, we can keep track of the paths with the
        # most empty cells which are also the min obstacles to remove
        ROWS, COLS = len(grid), len(grid[0])
        queue = [(0, 0, 0)]
        visited = set([(0, 0)])

        while queue:
            dist, i, j = heapq.heappop(queue)
            if i == ROWS - 1 and j == COLS - 1:
                return dist
            if i - 1 in range(ROWS) and (i - 1, j) not in visited:
                heapq.heappush(queue, (dist + grid[i - 1][j], i - 1, j))
                visited.add((i - 1, j))
            if i + 1 in range(ROWS) and (i + 1, j) not in visited:
                heapq.heappush(queue, (dist + grid[i + 1][j], i + 1, j))
                visited.add((i + 1, j))
            if j - 1 in range(COLS) and (i, j - 1) not in visited:
                heapq.heappush(queue, (dist + grid[i][j - 1], i, j - 1))
                visited.add((i, j - 1))
            if j + 1 in range(COLS) and (i, j + 1) not in visited:
                heapq.heappush(queue, (dist + grid[i][j + 1], i, j + 1))
                visited.add((i, j + 1))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[0, 1, 1], [1, 1, 0], [1, 1, 0]],
        [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumObstacles(*puzzle))
