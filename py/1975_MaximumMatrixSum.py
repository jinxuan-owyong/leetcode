# 1975. Maximum Matrix Sum

from utils import chunk
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        given an odd number of negative numbers in the matrix, regardless of how many 
        operations performed, there will be 1 negative number remaining
        [ 1, -1,  1]      [ 1, 1,  1]
        [-1, -5, -1] -->  [-1, 5,  1]
        [ 1, -1,  1]      [ 1, 1,  1]

        to find the maximum sum, we count the number of negative numbers, as well as
        the absolute sum of the matrix
        2x since we added the positive value of the smallest negative
        if odd  -> absolute sum - 2x smallest absolute value
        if even -> absolute sum
        """
        smallest = float('inf')
        total = 0
        oddNegative = False

        for row in matrix:
            for el in row:
                total += abs(el)
                smallest = min(abs(el), smallest)
                if el < 0:
                    oddNegative = not oddNegative

        return total - ((2 * smallest) if oddNegative else 0)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, -1], [-1, 1]],
        [[1, 2, 3], [-1, -2, -3], [1, 2, 3]],
        [[1, -1, 1], [-1, -5, -1], [1, -1, 1]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxMatrixSum(*puzzle))
