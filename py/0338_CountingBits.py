# 338. Counting Bits

from utils import chunk
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n+1)
        for i in range(n+1):
            bits[i] = (i & 1) + bits[i >> 1]
        return bits


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        2,
        5,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countBits(*puzzle))
