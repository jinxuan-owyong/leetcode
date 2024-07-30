# 2976. Minimum Cost to Convert String I

from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # find shortest path between changes
        # maximum of 26 characters
        dist = [[1E10 for _ in range(26)] for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0

        for c1, c2, c3 in zip(original, changed, cost):
            n1 = ord(c1) - ord("a")
            n2 = ord(c2) - ord("a")
            # possible to have multiple costs
            dist[n1][n2] = min(dist[n1][n2], c3)

        for mid in range(26):
            for src in range(26):
                for tgt in range(26):
                    dist[src][tgt] = min(
                        dist[src][tgt], dist[src][mid] + dist[mid][tgt])

        # find necessary conversions and update cost
        totalCost = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            src = ord(source[i]) - ord("a")
            tgt = ord(target[i]) - ord("a")
            if dist[src][tgt] == 1E10:
                return -1
            totalCost += dist[src][tgt]

        return totalCost


if __name__ == "__main__":
    puzzles = [
        ("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], [
         "b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]),
        ("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]),
        ("abcd", "abce", ["a"], ["e"], [10000])
    ]
    for puzzle in puzzles:
        print(Solution().minimumCost(*puzzle))

"""
Runtime
1955
ms
Beats
36.55%
Memory
18.41
MB
Beats
27.92%
"""