# 1976. Number of Ways to Arrive at Destination

from utils import chunk
from typing import List
import heapq


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # use dijkstra's algorithm to identify the shortest path to node n-1
        # keep track of the number of ways to reach node i, then increment the count of node i+1
        adjList = {i: [] for i in range(n)}
        for u, v, w in roads:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        visited = set()
        dist = [float("inf")] * n
        count = [0] * n
        dist[0] = 0
        count[0] = 1
        pq = [(0, 0)]  # weight, node
        while pq:
            _, curr = heapq.heappop(pq)
            if curr not in visited:
                visited.add(curr)
                for nei, weight in adjList[curr]:
                    if weight + dist[curr] < dist[nei]: # normal dijkstra case
                        dist[nei] = weight + dist[curr]
                        heapq.heappush(pq, (dist[nei], nei))
                        count[nei] = count[curr] # same since number of ways to reach a node depends on previous
                    elif weight + dist[curr] == dist[nei]: # modified to account for same weighted paths
                        # if we have already found a path of same distance, we want to retian the count of the equally optimal path
                        # if a new lower cost is found later, this will be overwritten in the if case
                        count[nei] += int(count[curr] % (1E9+7))
                        
        return int(count[-1] % (1E9+7))


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        7,
        [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [
            3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]],
        2,
        [[1, 0, 10]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countPaths(*puzzle))
