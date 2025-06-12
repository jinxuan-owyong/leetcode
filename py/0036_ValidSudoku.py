# 36. Valid Sudoku

from utils import chunk
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid3x3(i, j):
            cells = set()
            for y in range(i, i+3):
                for x in range(j, j+3):
                    if (cell := board[y][x]) in cells and cell != '.':
                        return False
                    cells.add(board[y][x])
            return True

        def isValidRow(i):
            cells = set()
            for j in range(COLS):
                if (cell := board[i][j]) in cells and cell != '.':
                    return False
                cells.add(board[i][j])
            return True

        def isValidCol(j):
            cells = set()
            for i in range(ROWS):
                if (cell := board[i][j]) in cells and cell != '.':
                    return False
                cells.add(board[i][j])
            return True

        # given top-left cell of a 3x3 grid, check for duplicates in grid
        # further improvement: we can combine this into 1 loop, since the grid is a square
        # to map a cell to it's 3x3 identifier, take (i //3 , j // 3)
        ROWS, COLS = len(board), len(board[0])

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not valid3x3(i, j):
                    return False

        return all(map(isValidRow, range(ROWS))) and \
            all(map(isValidCol, range(COLS)))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [["1", "2", ".", ".", "3", ".", ".", ".", "."],
         ["4", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", ".", "3"],
         ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
         [".", ".", ".", "8", ".", "3", ".", ".", "5"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", ".", ".", ".", ".", ".", "2", ".", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "8"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]],

        [["1", "2", ".", ".", "3", ".", ".", ".", "."],
         ["4", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", "9", "1", ".", ".", ".", ".", ".", "3"],
         ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
         [".", ".", ".", "8", ".", "3", ".", ".", "5"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", ".", ".", ".", ".", ".", "2", ".", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "8"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().isValidSudoku(*puzzle))
