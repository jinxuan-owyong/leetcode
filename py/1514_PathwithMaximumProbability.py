# 1514. Path with Maximum Probability

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            # undirected edges
            adjList[u].append((v, succProb[i]))
            adjList[v].append((u, succProb[i]))

        visited = [False] * n
        result = [0] * n
        result[start_node] = 1
        pq = [(-1, start_node)]  # probability, node - max heap

        # dijkstra's algorithm
        while pq:
            curr, node = heapq.heappop(pq)
            curr *= -1
            if visited[node]:
                continue
            visited[node] = True
            for neighbour, cost in adjList[node]:
                # if probability can be improved
                if result[neighbour] < curr * cost:
                    result[neighbour] = curr * cost
                    if not visited[neighbour]:
                        heapq.heappush(pq, (-curr * cost, neighbour))

        return result[end_node]


if __name__ == "__main__":
    puzzles = [
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2),
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2),
        (3, [[0, 1]], [0.5], 0, 2),
        (5, [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
         [0.37, 0.17, 0.93, 0.23, 0.39, 0.04], 3, 4)
    ]
    for puzzle in puzzles:
        print(Solution().maxProbability(*puzzle))
