# 1331. Rank Transform of an Array

from utils import chunk
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank, prev, i = {}, None, 0
        for curr in sorted(arr):
            if curr != prev:
                i += 1
            rank[curr] = i
            prev = curr
        return [rank[num] for num in arr]


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [40, 10, 20, 30],
        [100, 100, 100],
        [37, 12, 28, 9, 100, 56, 80, 5, 12]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().arrayRankTransform(*puzzle))
