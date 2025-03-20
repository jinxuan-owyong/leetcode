# 3108. Minimum Cost Walk in Weighted Graph

from utils import chunk
from typing import List


class Solution:
    class UnionFind:
        # to find connected components
        def __init__(self, size: int):
            # initially, every node is its own parent
            self.parent = list(range(size))
            self.rank = [0] * size

        def find(self, i: int) -> int:
            # find the parent of node i
            p = self.parent[i]
            # path compression: shorten height of tree during traversal -> set child's parent to its grandparent
            while p != self.parent[p]:
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]
            return p

        def union(self, i: int, j: int) -> bool:
            # join nodes if they have different parents
            p1, p2 = self.find(i), self.find(j)
            if p1 == p2:
                return False

            # union by rank - smaller rank should be child of larger rank
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:  # adding same rank results in an increased rank
                self.parent[p2] = p1
                self.rank[p1] += 1

            return True

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # use union find to identify connected components
        uf = self.UnionFind(n)
        for u, v, w in edges:
            # an edge represents a union
            uf.union(u, v)

        # the minimum cost walk is the bitwise AND of all edge weights of the connected component
        # group nodes of the same component together
        cost = {}
        for u, v, w in edges:
            if (parent := uf.find(u)) == uf.find(v):
                if parent in cost:
                    cost[parent] &= w
                else:
                    cost[parent] = w

        result = []
        for u, v in query:
            if (parent := uf.find(u)) == uf.find(v):
                result.append(cost[parent])
            else:
                # different parents mean there is no valid walk
                result.append(-1)

        return result


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        5,
        [[0, 1, 7], [1, 3, 7], [1, 2, 1]],
        [[0, 3], [3, 4]],
        3,
        [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]],
        [[1, 2]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumCost(*puzzle))
