# 743. Network Delay Time

from utils import chunk
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        given source node k, we can perform sssp using dijkstra's algorithm
        to determine the shortest path to a node
        then verify if all nodes have a valid time to receive signal
        """
        adjList = defaultdict(list)
        for u, v, w in times:
            adjList[u].append((v, w))

        dist = [float('inf')] * (n+1)
        dist[k] = 0
        pq = [(0, k)]
        visited = set()
        while pq:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            for nei, edge in adjList[node]:
                if dist[node] + edge < dist[nei]:
                    dist[nei] = dist[node] + edge
                heapq.heappush(pq, (dist[nei], nei))

        result = dist[1]
        for i in range(1, len(dist)):
            if dist[i] == float('inf'):
                return -1
            else:
                result = max(result, dist[i])
        return result


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
        4,
        2,
        [[1, 2, 1]],
        2,
        1,
        [[1, 2, 1]],
        2,
        2,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().networkDelayTime(*puzzle))
