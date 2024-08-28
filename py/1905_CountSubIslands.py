# 1905. Count Sub Islands

from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        NROWS, NCOLS = len(grid1), len(grid1[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def startingPoints():
            for i, row in enumerate(grid2):
                for j, el in enumerate(row):
                    if el == 1:
                        yield i, j

        # 4-directional DFS to find an island in grid2
        def dfs(i: int, j: int, visited: set):
            stack = [(i, j)]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                for dy, dx in DIRS:
                    y, x = curr[0] + dy, curr[1] + dx
                    if y in range(NROWS) and x in range(NCOLS) and grid2[y][x] == 1:
                        stack.append((y, x))

        def isSubIsland(cells: set):
            for y, x in cells:
                if grid1[y][x] == 0:
                    return False
            return True

        visited = set()
        result = 0
        for y, x in startingPoints():
            # only perform dfs if new island
            if (y, x) not in visited:
                # identify the cells belonging to an island in grid2
                currIsland = set()
                dfs(y, x, currIsland)
                visited.update(currIsland)
                if isSubIsland(currIsland):
                    result += 1

        return result


if __name__ == "__main__":
    puzzles = [
        ([[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
         [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]),
        ([[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
         [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]),
        ([[1, 1, 1]], [[1, 0, 1]]),
        ([[1, 0, 1]], [[1, 1, 1]])
    ]
    for puzzle in puzzles:
        print(Solution().countSubIslands(*puzzle))
