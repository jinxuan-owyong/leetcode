# 3243. Shortest Distance After Road Addition Queries I

from utils import chunk
from typing import List
from collections import deque


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adjList = [[i + 1] for i in range(n)]
        adjList[n - 1].pop()

        def bfs():
            queue = deque([(0, 0)])
            visited = [False] * n
            lowest = float('inf')

            while queue:
                for _ in range(len(queue)):
                    curr, dist = queue.popleft()
                    if visited[curr]:
                        continue
                    elif curr == n - 1:
                        lowest = min(lowest, dist)
                    else:
                        for nei in adjList[curr]:
                            queue.append((nei, dist + 1))
                            visited[curr] = True

            return lowest

        result = []
        for u, v in queries:
            adjList[u].append(v)
            result.append(bfs())

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        5, [[2, 4], [0, 2], [0, 4]],
        4, [[0, 3], [0, 2]],
        14, [[0, 6], [4, 12]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().shortestDistanceAfterQueries(*puzzle))
