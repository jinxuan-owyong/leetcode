# 2033. Minimum Operations to Make a Uni-Value Grid

from utils import chunk
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        consider 2 numbers a and b. to make them equal, abs(a-b) must be some multiple of x, otherwise it's not possible
        to minimise the number of operations, work towards the median value of the grid -> average is not desirable due to skewing
        sort the values of grid to quickly identify the median
        """
        values = sorted(el for row in grid for el in row)

        if len(values) == 1:
            return 0

        mid = len(values) // 2
        result = float('inf')
        for median in set(values[mid-1:mid+1]):  # 2 possible median values
            curr = 0
            valid = True
            for value in values:
                diff = abs(value - median)
                if diff % x == 0:
                    curr += diff // x
                else:
                    valid = False
                    break
            if valid and curr < result:
                result = curr

        return result if result < float('inf') else -1


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [[2, 4], [6, 8]],
        2,
        [[1, 5], [2, 3]],
        1,
        [[1, 2], [3, 4]],
        2,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minOperations(*puzzle))
