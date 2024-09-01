# 2022. Convert 1D Array Into 2D Array

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = original[i * n + j]
        return result


if __name__ == "__main__":
    numInputsPerTestcase = 3
    puzzles = [
        ([1, 2, 3, 4], 2, 2),
        ([1, 2, 3], 1, 3),
        ([1, 2], 1, 1),
        ([1, 2, 3, 4], 2, 3)
    ]
    for puzzle in puzzles:
        print(Solution().construct2DArray(*puzzle))
