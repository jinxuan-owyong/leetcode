# 840. Magic Squares In Grid


from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if min(len(grid), len(grid[0])) < 3:
            return 0

        count = 0
        expected = set(range(1, 10))
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                actual = set([grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1], grid[i][j - 1],
                             grid[i][j], grid[i][j + 1], grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]])

                row1sum = grid[i - 1][j - 1] + \
                    grid[i - 1][j] + grid[i - 1][j + 1]
                row2sum = grid[i][j - 1] + grid[i][j] + grid[i][j + 1]
                row3sum = grid[i + 1][j - 1] + \
                    grid[i + 1][j] + grid[i + 1][j + 1]
                isRowSumEqual = row1sum == row2sum and row2sum == row3sum

                col1sum = grid[i - 1][j - 1] + \
                    grid[i][j - 1] + grid[i + 1][j - 1]
                col2sum = grid[i - 1][j] + grid[i][j] + grid[i + 1][j]
                col3sum = grid[i - 1][j + 1] + \
                    grid[i][j + 1] + grid[i + 1][j + 1]
                isColSumEqual = col1sum == col2sum and col2sum == col3sum

                diagonal1sum = grid[i - 1][j - 1] + \
                    grid[i][j] + grid[i + 1][j + 1]
                diagonal2sum = grid[i + 1][j - 1] + \
                    grid[i][j] + grid[i - 1][j + 1]
                isDiagonalSumEqual = diagonal1sum == diagonal2sum

                isMagicSquare = (expected ==
                                 actual and isRowSumEqual and isColSumEqual and isDiagonalSumEqual)

                count += 1 if isMagicSquare else 0

        return count


if __name__ == "__main__":
    puzzles = [
        [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]],
        [[8]]
    ]
    for puzzle in puzzles:
        print(Solution().numMagicSquaresInside(puzzle))
