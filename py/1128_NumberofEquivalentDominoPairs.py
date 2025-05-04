# 1128. Number of Equivalent Domino Pairs

from utils import chunk
from typing import List
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = defaultdict(int)
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            pairs[(a, b)] += 1
        # number of pairs that can be formed from n elements is 1 + 2 + ... + n-1 = 0.5*n*(n-1)
        return int(sum(0.5*n*(n-1) for n in pairs.values() if n > 1))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 2], [2, 1], [3, 4], [5, 6]],
        [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().numEquivDominoPairs(*puzzle))
