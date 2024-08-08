# 885. Spiral Matrix III


from typing import List
from enum import Enum


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        DIRECTION = Enum("DIR", names="NORTH SOUTH EAST WEST")
        i, j = rStart, cStart
        radius = 0
        maxRadius = max(rStart, rows - rStart - 1, cStart, cols - cStart - 1)

        def travelInDirection(dir: DIRECTION, y: int, x: int, radius: int):
            # | E S W N | E S W N | E S W N | ...
            # | 1 1 2 2 | 3 3 4 4 | 5 5 6 6 | ...
            # 2r - 1, 2r
            isEastOrSouth = dir == DIRECTION.EAST or dir == DIRECTION.SOUTH
            cells = (2 * radius - 1) if isEastOrSouth else (2 * radius)

            match dir:
                case DIRECTION.EAST:
                    return y, x + cells
                case DIRECTION.SOUTH:
                    return y + cells, x
                case DIRECTION.WEST:
                    return y, x - cells
                case DIRECTION.NORTH:
                    return y - cells, x

        def getCellsTravelled(dir: DIRECTION, y1: int, x1: int, y2: int, x2: int) -> List[List[int]]:
            def isWithinGrid(y: int, x: int) -> bool:
                return y in range(rows) and x in range(cols)

            # return path traversed excluding current position to prevent duplicates
            match dir:
                case DIRECTION.EAST:
                    return [[y1, x] for x in range(x1 + 1, x2 + 1) if isWithinGrid(y1, x)]
                case DIRECTION.SOUTH:
                    return [[y, x1] for y in range(y1 + 1, y2 + 1) if isWithinGrid(y, x1)]
                case DIRECTION.WEST:
                    return [[y1, x] for x in range(x1 - 1, x2 - 1, -1) if isWithinGrid(y1, x)]
                case DIRECTION.NORTH:
                    return [[y, x1] for y in range(y1 - 1, y2 - 1, -1) if isWithinGrid(y, x1)]

        visited = [[i, j]]
        # edge case: traversal ends in DIRECTION.EAST - require additional iteration
        for radius in range(1, maxRadius + 2):
            for dir in [DIRECTION.EAST, DIRECTION.SOUTH, DIRECTION.WEST, DIRECTION.NORTH]:
                # take 1 extra step to prevent cycle
                a, b, (i, j) = i, j, travelInDirection(dir, i, j, radius)
                visited.extend(getCellsTravelled(dir, a, b, i, j))

        return visited


if __name__ == "__main__":
    puzzles = [
        (1, 4, 0, 0),
        (5, 6, 1, 4),
        (3, 3, 1, 1)
    ]
    for puzzle in puzzles:
        print(Solution().spiralMatrixIII(*puzzle))
