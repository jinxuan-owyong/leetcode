# 191. Number of 1 Bits

from utils import chunk


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 0b1
            n >>= 1
        return count


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        11,
        128,
        2147483645
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().hammingWeight(*puzzle))
