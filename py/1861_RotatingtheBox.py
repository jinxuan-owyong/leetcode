# 1861. Rotating the Box

from utils import chunk
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        STONE, OBSTACLE, EMPTY = "#", "*", "."

        def countStones(row: List[str], start: int) -> List[int]:
            stones = 0
            curr = start
            while curr < len(row) and row[curr] != OBSTACLE:
                stones += 1 if row[curr] == STONE else 0
                curr += 1
            return curr, stones, curr - start - stones  # start, stones, empty

        def stoneFallResult(row: List[str]) -> List[str]:
            try:
                start = row.index(STONE)
            except ValueError:
                return row

            result = row[:start]
            # count stones/empty until the next obstacle
            while start < len(row):
                if row[start] == OBSTACLE:
                    result.append(OBSTACLE)
                    start += 1
                else:
                    start, numStones, numEmpty = countStones(row, start)
                    result.extend([EMPTY] * numEmpty + [STONE] * numStones)

            return result

        # initially, "gravity" is to the right
        # then by reversing and transposing the matrix, we can rotate right by 90 degrees
        fallen = reversed(list(map(stoneFallResult, box)))
        transposed = [[EMPTY] * len(box) for _ in range(len(box[0]))]
        for i, row in enumerate(fallen):
            for j, el in enumerate(row):
                transposed[j][i] = el

        return transposed


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [["#", ".", "#"]],
        [["#", ".", "*", "."], ["#", "#", "*", "."]],
        [["#", "#", "*", ".", "*", "."],
         ["#", "#", "#", "*", ".", "."],
         ["#", "#", "#", ".", "#", "."]],
        [['#']],
        [['.'], ['*'], ['#']]
    ]
    for puzzle in chunk(puzzles, testSize):
        m = Solution().rotateTheBox(*puzzle)
        [print(row) for row in m]
        print()
