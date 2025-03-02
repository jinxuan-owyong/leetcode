# 2570. Merge Two 2D Arrays by Summing Values

from utils import chunk
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # merge and sum values in both arrays
        # since 1 <= id <= 1000, we can store the sum in a list
        total = [0] * (1000 + 1)
        for id, val in nums1:
            total[id] += val
        for id, val in nums2:
            total[id] += val
        return [[i, count] for i, count in enumerate(total) if count > 0]


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [[1, 2], [2, 3], [4, 5]],
        [[1, 4], [3, 2], [4, 1]],
        [[2, 4], [3, 6], [5, 5]],
        [[1, 3], [4, 3]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().mergeArrays(*puzzle))
