# 959. Regions Cut By Slashes


from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # initialise 3n x 3m cells to represent slashes with 3x3 binary
        cells = [[0] * 3 * len(grid[0]) for _ in range(len(grid) * 3)]
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "/":
                    cells[3 * i][(3 * j) + 2] = 1
                    cells[(3 * i) + 1][(3 * j) + 1] = 1
                    cells[(3 * i) + 2][3 * j] = 1
                elif c == "\\":
                    cells[3 * i][3 * j] = 1
                    cells[(3 * i) + 1][(3 * j) + 1] = 1
                    cells[(3 * i) + 2][(3 * j) + 2] = 1

        # number of islands
        islands = 0
        NROWS, NCOLS = len(cells), len(cells[0])

        def dfs(i: int, j: int):
            stack = [(i, j)]
            while stack:
                curr = stack.pop()

                for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    y, x = curr[0] + dy, curr[1] + dx
                    isValidUnvisted = y in range(NROWS) and x in range(NCOLS)
                    if isValidUnvisted and cells[y][x] == 0:
                        stack.append((y, x))
                        cells[y][x] = -1  # mark as visited

        for i in range(NROWS):
            for j in range(NCOLS):
                if cells[i][j] == 0:
                    dfs(i, j)
                    islands += 1

        return islands


if __name__ == "__main__":
    puzzles = [
        [" /", "/ "],
        [" /", "  "],
        ["/\\", "\\/"]
    ]
    for puzzle in puzzles:
        print(Solution().regionsBySlashes(puzzle))
