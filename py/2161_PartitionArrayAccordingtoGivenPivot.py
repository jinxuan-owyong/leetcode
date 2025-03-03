# 2161. Partition Array According to Given Pivot

from utils import chunk
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        numPivot = 0
        left, right = [], []

        for n in nums:
            if n == pivot:
                numPivot += 1
            elif n < pivot:
                left.append(n)
            else:
                right.append(n)

        left.extend([pivot] * numPivot)
        left.extend(right)

        return left


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [9, 12, 5, 10, 14, 3, 10], 10,
        [-3, 4, 3, 2], 2,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().pivotArray(*puzzle))
