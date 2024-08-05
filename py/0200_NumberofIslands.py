# 200. Number of Islands

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i: int, j: int):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                grid[i][j] = "v"  # mark cell as visited

                for dy, dx in DIRS:
                    y, x = i + dy, j + dx

                    if y not in range(len(grid)) or \
                            x not in range(len(grid[0])):
                        continue

                    if grid[y][x] == "1":  # also checks if visited since we use "v"
                        stack.append((y, x))

        count = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "1" and grid[i][j] != "v":
                    dfs(i, j)
                    count += 1

        return count


if __name__ == "__main__":
    puzzles = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    ]
    for puzzle in puzzles:
        print(Solution().numIslands(puzzle))

"""
Runtime
300
ms
Beats
19.60%
Memory
18.96
MB
Beats
57.51%
"""
