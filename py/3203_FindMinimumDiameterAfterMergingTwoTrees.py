# 3203. Find Minimum Diameter After Merging Two Trees

from utils import chunk
from typing import Dict, List
from collections import defaultdict
import heapq
import math


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        """
        to minimise the diameter of the final tree, we need to join the 2 trees at their "center"
        let node 0 be the root
        take the longest 2 root-to-leaf distances ("radius"), sum to get the diameter
        with the diameter, we can "fold the longest path in half" to obtain the center-to-leaf distance
        this distance is added together and + 1 for the additional connecting edge
        """

        def buildAL(edges: List[List[int]]) -> Dict[int, List[int]]:
            adjList = defaultdict(list)
            for u, v in edges:
                adjList[u].append(v)
                adjList[v].append(u)
            return adjList

        def findDiameter(adjList: Dict[int, List[int]], curr: int, parent: int, diameter: List[int]):
            # the top 2 deepest children give us the longest diameter of the tree
            depths = [0, 0]  # min-heap

            for nei in adjList[curr]:
                if nei == parent:
                    continue
                childDepth = findDiameter(adjList, nei, curr, diameter)
                heapq.heappushpop(depths, childDepth)

            diameter[0] = max(diameter[0], sum(depths))
            return 1 + depths[1]  # heap size is 2

        adjList1, adjList2 = buildAL(edges1), buildAL(edges2)
        d1, d2 = [0], [0]
        findDiameter(adjList1, 0, -1, d1)
        findDiameter(adjList2, 0, -1, d2)
        r1, r2 = math.ceil(d1[0] / 2), math.ceil(d2[0] / 2)
        return max(d1[0], d2[0], r1 + r2 + 1)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [[0, 1], [0, 2], [0, 3]],
        [[0, 1]],
        [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
        [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumDiameterAfterMerge(*puzzle))
