# 2220. Minimum Bit Flips to Convert Number

from utils import chunk


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        # XOR == 1 if both bits do not match
        start ^= goal
        while start:
            count += start & 0b1
            start >>= 1
        return count


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        10,
        7,
        3,
        4,
        0,
        0,
        0,
        3
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minBitFlips(*puzzle))
