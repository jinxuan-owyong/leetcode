# 695. Max Area of Island


from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # get starting points
        starting_points = []
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    starting_points.append((i, j))

        visited = set()
        max_area = 0
        for start in starting_points:
            if start in visited:
                continue

            island_area = 0
            stack = [start]
            visited.add(start)
            while stack:
                curr = stack.pop()
                island_area += 1  # assume that curr is "1"

                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    y, x = curr[0] + dy, curr[1] + dx
                    is_valid_coord = y in range(
                        len(grid)) and x in range(len(grid[0]))
                    if is_valid_coord and (y, x) not in visited and grid[y][x] == 1:
                        stack.append((y, x))
                        visited.add((y, x))

            max_area = max(max_area, island_area)

        return max_area


if __name__ == "__main__":
    puzzles = [
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ],
        [[0, 0, 0, 0, 0, 0, 0, 0]]
    ]
    for puzzle in puzzles:
        print(Solution().maxAreaOfIsland(puzzle))
