# 1368. Minimum Cost to Make at Least One Valid Path in a Grid

from utils import chunk
from typing import List
import heapq
from collections import deque


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        to minimise the number of direction changes. longer routes are not penalised
        we can only modify a cell once
        explore all possible directions from cell with shortest path
        penalise changes in direction by adding 1, but add these 3 into the pq
        with the pq, we favour lower costs even if they take a longer path
        """
        ROWS, COLS = len(grid), len(grid[0])
        move = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]  # right left down up
        cost = [[float('inf')] * COLS for _ in range(ROWS)]
        pq = [(0, 0, 0)]  # start, cost
        while pq:
            dist, i, j = heapq.heappop(pq)
            if i == ROWS - 1 and j == COLS - 1:
                return dist
            for d in range(1, 5):
                dy, dx = move[d]
                y, x = i + dy, j + dx
                newDist = dist + (0 if d == grid[i][j] else 1)
                if y in range(ROWS) and x in range(COLS) and newDist < cost[y][x]:
                    # we only want cells that will improve the distance
                    cost[y][x] = newDist
                    heapq.heappush(pq, (newDist, y, x))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]],
        [[1, 1, 3], [3, 2, 2], [1, 1, 4]],
        [[1, 2], [4, 3]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minCost(*puzzle))
