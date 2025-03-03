# 54. Spiral Matrix

from utils import chunk
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        y, x = 0, -1  # start from "outside" the grid
        top, left, bot, right = 0, 0, len(
            matrix)-1, len(matrix[0])-1  # limits of y, x
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        curr = 0

        # we only need to extract m*n cells
        for _ in range(len(matrix) * len(matrix[0])):
            dy, dx = dirs[curr]
            isY, isX = y+dy in range(top, bot+1), x+dx in range(left, right+1)

            # change direction and shrink edges if next step results in out of bounds
            if not isY or not isX:
                match curr:
                    case 0:
                        top += 1
                    case 1:
                        right -= 1
                    case 2:
                        bot -= 1
                    case 3:
                        left += 1
                curr = (curr + 1) % 4

            dy, dx = dirs[curr]
            y, x = y+dy, x+dx
            result.append(matrix[y][x])

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[1]],
        [[1, 2, 3, 4]],
        [[1], [2], [3], [4]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().spiralOrder(*puzzle))
