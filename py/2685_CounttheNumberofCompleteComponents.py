# 2685. Count the Number of Complete Components

from utils import chunk
from typing import List
from collections import defaultdict


class Solution:
    class UnionFind:
        def __init__(self, size: int):
            self.parent = {p: p for p in range(size)}
            self.rank = defaultdict(int)

        def find(self, u: int) -> int:
            p = self.parent[u]
            # path compression
            while p != self.parent[p]:
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]
            return p

        def union(self, u: int, v: int) -> bool:
            p1, p2 = self.find(u), self.find(v)
            if p1 == p2:
                return False
            # union by rank -> larger is parent of smaller
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p1] = p2
                self.rank[p2] += 1
            return True

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        use union find to identify connected components in the graph
        a connected component is a complete graph if it has (n * (n-1))//2 edges
        """
        outdegree = [0] * n
        uf = self.UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
            outdegree[u] += 1
            outdegree[v] += 1

        # count nodes of a connected component, using parent as a unique identifier
        componentNodes = defaultdict(int)
        for u in uf.parent:
            p = uf.find(u)
            componentNodes[p] += 1

        # if a connected component has n nodes, each node should have n-1 edges to be a complete component
        complete = {p: True for p in componentNodes}
        for u in uf.parent:
            p = uf.find(u)
            complete[p] = complete[p] and outdegree[u] == componentNodes[p]-1

        return sum(1 for p in complete if complete[p])


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        6,
        [[0, 1], [0, 2], [1, 2], [3, 4]],
        6,
        [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]],
        5,
        [[1, 2], [3, 4], [1, 4], [2, 3], [1, 3], [2, 4]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countCompleteComponents(*puzzle))
