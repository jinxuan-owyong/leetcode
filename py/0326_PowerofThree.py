# 326. Power of Three

from utils import chunk


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(20):  # 3^19 < 2^31 - 1 < 3^20
            if 3 ** i == n:
                return True
        return False


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        27,
        0,
        -1,
        1594323,
        1594322,
        # *[3 ** i for i in range(19)]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().isPowerOfThree(*puzzle))
