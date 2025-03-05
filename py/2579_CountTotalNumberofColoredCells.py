# 2579. Count Total Number of Colored Cells

from utils import chunk


class Solution:
    def coloredCells(self, n: int) -> int:
        # 1, 1+4, 1+4+8, 1+4+8+12, ..., 1+4*1+4*2+4*3+...+4*n
        # = 1 + 4(0+1+2+3, ... , + n) = 1 + (n/2) * (2*0+(n-1)*4)
        # arithmetic sum: a = 0, d = 4
        # (n/2)*(2a+(n-1)d)
        return int(1 + (n/2) * (n-1)*4)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().coloredCells(*puzzle))
