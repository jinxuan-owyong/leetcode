# 2657. Find the Prefix Common Array of Two Arrays

from utils import chunk
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        left, right = set([A[0]]), set([B[0]])

        for i in range(len(A)):
            left.add(A[i])
            right.add(B[i])
            C.append(len(left.intersection(right)))

        return C


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 3, 2, 4], [3, 1, 2, 4],
        [2, 3, 1], [3, 1, 2],
        [1], [1],
        [1], [2]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findThePrefixCommonArray(*puzzle))
