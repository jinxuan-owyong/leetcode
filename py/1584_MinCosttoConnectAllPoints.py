# 1584. Min Cost to Connect All Points

from utils import chunk
from typing import List
from collections import defaultdict
import heapq


class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.rank = defaultdict(int)

        def find(self, i):
            if i not in self.parent:  # initially, each node is its own parent
                self.parent[i] = i

            p = self.parent[i]
            # path compression
            while p != self.parent[p]:
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]
            return p

        def union(self, i, j) -> bool:
            p1, p2 = self.find(i), self.find(j)
            # both nodes are from the same subcomponent
            if p1 == p2:
                return False
            # join the lower ranked connected component to the higher ranked
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                # assign either, then increment rank of the other
                self.parent[p1] = p2
                self.rank[p2] += 1
            return True

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        find minimum spanning tree with kruskal's algorithm
        each point represents a node in the graph
        generate the possible connections to every other node
        then find MST edges until we have len(points)-1 edges
        """
        uf = self.UnionFind()
        connections = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)  # manhattan distance
                heapq.heappush(connections, (dist, i, j))
            # make each node hashable for union find
            points[i] = tuple(points[i])

        edges = 0
        result = 0
        while edges < len(points)-1:
            dist, u, v = heapq.heappop(connections)
            if uf.union(points[u], points[v]):
                result += dist
                edges += 1

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],
        [[3, 12], [-2, 5], [-4, 1]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minCostConnectPoints(*puzzle))
