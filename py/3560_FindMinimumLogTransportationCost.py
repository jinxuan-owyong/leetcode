# 3560. Find Minimum Log Transportation Cost

from utils import chunk


class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        # 1 <= n, m <= 2 * k
        # logs are at most 2x the length of the truck
        cost = 0
        if n > k:
            cost += (n-k)*k
            n -= k
        else:
            n = 0
        if m > k:
            cost += (m-k)*k
            m -= k
        else:
            m = 0

        # cannot transport remaining in 1 truck
        # split the shorter log (n)
        n, m = min(n, m), max(n, m)
        if n + m > k:
            cut = min(k-m, n)
            cost += (n-cut)*cut

        return cost


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        6, 5, 5, 
        4, 4, 6,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minCuttingCost(*puzzle))
