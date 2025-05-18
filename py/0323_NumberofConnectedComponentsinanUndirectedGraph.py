# 323. Number of Connected Components in an Undirected Graph

from utils import chunk
from typing import List


class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, u):
            p = self.parent[u]
            while p != self.parent[p]:
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]
            return p

        def union(self, u, v):
            p1, p2 = self.find(u), self.find(v)
            if p1 == p2:
                return False
            # union by rank
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
                self.rank[p1] += 1
            return True

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = self.UnionFind(n)
        # assume all components are not connected initially
        # each successful union reduces the total number of connected components by 1
        components = n
        for u, v in edges:
            if uf.union(u, v):
                components -= 1
        return components


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        3, [[0, 1], [0, 2]],
        6, [[0, 1], [1, 2], [2, 3], [4, 5]],
        6, [[0, 1], [2, 3], [4, 5], [1, 2], [3, 4]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countComponents(*puzzle))
