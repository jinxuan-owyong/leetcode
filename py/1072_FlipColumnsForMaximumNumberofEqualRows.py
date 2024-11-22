# 1072. Flip Columns For Maximum Number of Equal Rows

from utils import chunk
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        to achieve equal rows after flipping, each of the rows need to have a similar pattern
        before the flip such that each group of "0"s or "1"s in the same column are similar
        across rows - then flipping will result in rows with the same element

        no flipping is required, but instead we identify how the "0"s and "1"s are grouped in
        each of the matrix rows. the maximum number of rows is the count of the most common pattern
        using SAME to denote groups with the bit and DIVIDER to separate SAME groups, we can create
        a bit pattern of a given row
        SAME, DIVIDER = 1, 0
        [0, 0, 1, 0, 1] -> 11 0 1 0 1 0 1
        [0, 0, 0] -> 111
        [1, 0, 0] -> 1 0 11
        """

        def getPattern(row: List[int]) -> int:
            pattern = 1
            for i in range(1, len(row)):
                # shift left by 2 to insert extra "0"
                shift = 1 if row[i] == row[i - 1] else 2
                pattern = (pattern << shift) | 1
            return pattern

        freq = {}
        largest = 0
        for pattern in map(getPattern, matrix):
            count = freq.get(pattern, 0) + 1
            freq[pattern] = count
            largest = max(count, largest)

        return largest


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[0, 1], [1, 1]],
        [[0, 1], [1, 0]],
        [[0, 0, 0], [0, 0, 1], [1, 1, 0]],
        [[0, 0, 1, 0, 1], [1, 1, 0, 1, 0], [0, 0, 1, 0, 1]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxEqualRowsAfterFlips(*puzzle))
