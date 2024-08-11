# 1568. Minimum Number of Days to Disconnect Island


from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        NROWS, NCOLS = len(grid), len(grid[0])

        def dfs(visited: set, startY: int, startX: int):
            stack = [(startY, startX)]
            while stack:
                i, j = stack.pop()
                visited.add((i, j))
                for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    y, x = i + dy, j + dx
                    if (y, x) not in visited and y in range(NROWS) and x in range(NCOLS) and grid[y][x] == 1:
                        stack.append((y, x))

        def numIslands() -> int:
            visited = set()
            islands = 0
            for i, row in enumerate(grid):
                for j, cell in enumerate(row):
                    if cell == 1 and (i, j) not in visited:
                        dfs(visited, i, j)
                        islands += 1
            return islands, visited

        islands, islandCells = numIslands()
        if islands == 1 and len(islandCells) <= 2:
            return len(islandCells)
        elif islands > 1 or len(islandCells) == 0:
            return 0

        for i, j in islandCells:
            grid[i][j] = 0
            newCount, _ = numIslands()
            if newCount > 1:
                return 1
            grid[i][j] = 1

        # only up to 2 cells required to disconnect
        # by isolating a corner cell
        return 2


if __name__ == "__main__":
    puzzles = [
        [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
        [[1, 1]],
        [[0]],
        [[1]],
        [[0, 1]],
        [[0, 0], [1, 1]],
        [[0, 1], [1, 1]],
        [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]],
        [[0, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]],
        [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]
    ]
    for puzzle in puzzles:
        print(Solution().minDays(puzzle))
