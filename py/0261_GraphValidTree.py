# 261. Graph Valid Tree

from utils import chunk
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # should have n-1 edges
        if len(edges) != n-1:
            return False

        adjList = {i: list() for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)

        # should have no cycles - dfs cycle detection
        # choice of initial node does not matter since the graph is undirected
        visited = set()
        stack = [0]
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for nei in adjList[curr]:
                if nei in visited:
                    return False
                visited.add(nei)
                stack.append(nei)

        return True


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        5, [[0, 1], [0, 2], [0, 3], [1, 4]],
        5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().validTree(*puzzle))
