# 2275. Largest Combination With Bitwise AND Greater Than Zero

from utils import chunk
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        """
        [16,      17,      71,      62,      12,      24,      14      ]
         00010000 00010001 01000111 00111110 00001100 00011000 00001110

        numbers with bit[i]
        6: 71
        5: 62
        4: 16, 17, 62, 24
        3: 62, 12, 24, 14
        2: 71, 62, 12, 14
        1: 71, 62, 14
        0: 17, 71

        we want to perform as many bitwise AND operations as possible
        the result of the AND operation should contain only 1 bit for it to be
        as large as possible, so we return largest bit[i] count 
        since max candidates[i] is 10^7, max number of bits is 24
        using a bit mask for the ith bit, we can determine if it is present
        """
        count = [0] * 24

        for num in candidates:
            for i in range(24):
                count[i] += 1 if num & (1 << i) else 0

        return max(count)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [16, 17, 71, 62, 12, 24, 14],
        [8, 8],
        [1, 2],
        [2, 4, 8, 16, 32, 63]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().largestCombination(*puzzle))
