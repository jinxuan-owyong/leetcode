# 1310. XOR Queries of a Subarray

from utils import chunk
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefixXor[i + 1] = prefixXor[i] ^ arr[i]

        def query(q: List[int]) -> int:
            i, j = q[0], q[1]
            return prefixXor[i] ^ prefixXor[j + 1]

        return list(map(query, queries))


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 3, 4, 8],
        [[0, 1], [1, 2], [0, 3], [3, 3]],
        [4, 8, 2, 10],
        [[2, 3], [1, 3], [0, 0], [0, 3]],
        [3, 7],
        [[0, 0], [0, 1], [1, 1]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().xorQueries(*puzzle))
