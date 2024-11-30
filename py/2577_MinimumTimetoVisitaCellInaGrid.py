# 2577. Minimum Time to Visit a Cell In a Grid

from utils import chunk
from typing import List
import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # since we cannot even make 1 step, no oscillation can occur
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pq = [(0, 0, 0)]
        visited = set([(0, 0)])

        while pq:
            time, i, j = heapq.heappop(pq)
            if i == ROWS - 1 and j == COLS - 1:
                return time
            for dy, dx in DIRS:
                y, x = i + dy, j + dx
                if y in range(ROWS) and x in range(COLS) and (y, x) not in visited:
                    if time >= grid[y][x]:
                        # allowed to enter the current cell
                        heapq.heappush(pq, (time + 1, y, x))
                    else:
                        # oscillate between current and neighbouring to get the time to the next neighbour
                        # if difference between current time and grid[y][x] is odd, then the oscillation
                        # will land on grid[y][x] when it is equal to the "current" time
                        # otherwise it will take 1 extra step
                        oscillateTime = grid[y][x] + \
                            int((grid[y][x] - time) % 2 == 0)
                        heapq.heappush(pq, (oscillateTime, y, x))
                    visited.add((y, x))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]],
        [[0, 2, 4], [3, 2, 1], [1, 0, 4]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumTime(*puzzle))
