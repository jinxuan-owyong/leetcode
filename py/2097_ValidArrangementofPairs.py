# 2097. Valid Arrangement of Pairs

from utils import chunk
from typing import List
from collections import defaultdict
from collections import deque



class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        """
        Eulerian path/circuit explanation: https://www.youtube.com/watch?v=8MpoO2zA2l4
        An Eulerian path is a path of edges that visits all the edges exactly once
        to determine if an Eulerian path exists in a graph, we look at the in/outdegree
        either all nodes have the same in/outdegree, or for a single pair of nodes,
        (in[i] - out[i] > 1 and out[i] - in[i] > 1) and the rest have equal count.

        This means that the node with extra outgoing/incoming edge is the start/end node.
        an Eulerian circuit is where all in/outdegrees are equal, then any node with non-zero
        degree would serve as a suitable starting node.
        """
        inDegree = defaultdict(int)
        outDegree = defaultdict(int)
        adjList = defaultdict(list)  # adjList also counts the outDegree
        for u, v in pairs:
            inDegree[v] += 1
            outDegree[u] += 1
            adjList[u].append(v)

        # find odd edge count as start
        for u in adjList:
            # important property of Eulerian paths
            if outDegree[u] - inDegree[u] == 1:
                start = u
                break
            # make sure that we do not start on a node with no outgoing edge
            if outDegree[u] > 0:
                start = u

        path = []

        def dfs(i: int):
            # check if all edges have been visited
            if outDegree[i] == 0:
                return

            # use set to keep track of already visited nodes by removing them
            while adjList[i]:
                nei = adjList[i].pop()
                outDegree[i] -= 1
                dfs(nei)
                path.append([i, nei])

        dfs(start)
        return path[::-1]


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[5, 1], [4, 5], [11, 9], [9, 4]],
        [[1, 3], [3, 2], [2, 1]],
        [[1, 2], [1, 3], [2, 1]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().validArrangement(*puzzle))
