# 3342. Find Minimum Time to Reach Last Room II

from utils import chunk
from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROWS, COLS = len(moveTime), len(moveTime[0])

        pq = [(0, 0, 0, False)]
        visited = set([(0, 0)])
        while pq:
            time, i, j, two = heapq.heappop(pq)
            if (i, j) == (ROWS-1, COLS-1):
                return time

            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                y, x = i+dy, j+dx
                if y in range(ROWS) and x in range(COLS) and (y, x) not in visited:
                    # take maximum time since we cannot enter the cell until time is up
                    step = 2 if two else 1  # modification from # 3341, otherwise the same
                    heapq.heappush(
                        pq, (max(time+step, moveTime[y][x]+step), y, x, not two))
                    visited.add((y, x))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[0, 4], [4, 4]],
        [[0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 1], [1, 2]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minTimeToReach(*puzzle))
