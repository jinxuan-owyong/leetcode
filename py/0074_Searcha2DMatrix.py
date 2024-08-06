# 74. Search a 2D Matrix

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y, x = 0, len(matrix) - 1
        while y <= x:
            row = (y + x) // 2
            if target >= matrix[row][0] and target <= matrix[row][-1]:
                break
            elif target < matrix[row][-1]:
                x = row - 1
            else:
                y = row + 1

        i, j = 0, len(matrix[0]) - 1
        while i <= j:
            col = (i + j) // 2
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                j = col - 1
            else:
                i = col + 1

        return False


if __name__ == "__main__":
    puzzles = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
    ]
    for puzzle in puzzles:
        print(Solution().searchMatrix(*puzzle))
