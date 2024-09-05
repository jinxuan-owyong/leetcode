# 2028. Find Missing Observations

from utils import chunk
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        # mean is derived from sum of all rolls
        total = mean * (m + n)
        total -= sum(rolls)

        # maximum per roll is 6, hence maximum possible total is 6n
        if total < 1 or total > n * 6:
            return []

        # all rolls from here have a maximum of 6
        # there exists a dice number i where i * n <= total < (i + 1) * n and 1 <= i <= 6
        for i in range(1, 7):
            # result is within range
            if total >= i * n and total < (i + 1) * n:
                result = [i] * n
                curr = i * n
                j = 0
                while curr < total:
                    result[j] += 1
                    curr += 1
                    j += 1
                return result


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        [3, 2, 4, 3],
        4,
        2,
        [1, 5, 6],
        3,
        4,
        [1, 2, 3, 4],
        6,
        4,
        [1, 1],
        5,
        1
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().missingRolls(*puzzle))
