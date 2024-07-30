# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # find shortest path from city n to n + 1 using Floyd-Warshall's algorithm
        # https://www.youtube.com/watch?v=4OQeCuLYj-4
        dist = [[1E10 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for c1, c2, weight in edges:
            dist[c1][c2] = weight
            dist[c2][c1] = weight

        for mid in range(n):
            for src in range(n):
                for target in range(n):
                    # check if shorter path exists
                    dist[src][target] = min(
                        dist[src][target], dist[src][mid] + dist[mid][target])

        # filter cities that meet the distance threshold
        cityCount = {}
        for i in range(n):
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cityCount[i] = cityCount.get(i, 0) + 1
                    cityCount[j] = cityCount.get(j, 0) + 1

        # sort by least number of neighbouring cities and largest city number
        cityDist = min(cityCount.items(), key=lambda x: (x[1], -1 * x[0]))
        return cityDist[0]


if __name__ == "__main__":
    puzzles = [
        (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4),
        (5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2),
        (6, [[0, 3, 7], [2, 4, 1], [0, 1, 5], [
         2, 3, 10], [1, 3, 6], [1, 2, 1]], 417),
    ]
    for puzzle in puzzles:
        print(Solution().findTheCity(*puzzle))

"""
Runtime
474
ms
Beats
27.11%
Memory
17.64
MB
Beats
80.04%
"""
