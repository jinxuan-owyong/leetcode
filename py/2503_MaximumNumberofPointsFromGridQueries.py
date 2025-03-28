# 2503. Maximum Number of Points From Grid Queries

from utils import chunk
from typing import List
import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        perform BFS and calculate how many points a query "unlocks"
        repeat with the next query, adding on to the points from the current
        """
        ROWS, COLS = len(grid), len(grid[0])
        result = [0] * len(queries)
        visited = [[False] * COLS for _ in range(ROWS)]  # max 1000**2
        pq = [(grid[0][0], 0, 0)]
        prev = 0

        # sort by query value, order of query does not matter
        # the order of the result is preserved with idx
        for idx, query in sorted(enumerate(queries), key=lambda x: x[1]):
            count = 0
            # expand frontier until the current query is < the smallest discovered unprocessed cell
            while pq and pq[0][0] < query:
                _, i, j = heapq.heappop(pq)
                if not visited[i][j]:
                    visited[i][j] = True
                    count += 1
                    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        y, x = i + dy, j + dx
                        if y in range(ROWS) and x in range(COLS):
                            heapq.heappush(pq, (grid[y][x], y, x))

            result[idx] = prev + count
            prev += count

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [[1, 2, 3], [2, 5, 7], [3, 5, 1]],
        [5, 6, 2],
        [[5, 2, 1], [1, 1, 2]],
        [3],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxPoints(*puzzle))
