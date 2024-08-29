# 947. Most Stones Removed with Same Row or Column

from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        adjRow = defaultdict(list)
        adjCol = defaultdict(list)

        for y, x in stones:
            adjRow[y].append(x)
            adjCol[x].append(y)

        visited = set()

        def dfs(i: int, j: int) -> int:
            stack = [(i, j)]
            visited.add((i, j))
            count = 0

            while stack:
                curr = stack.pop()
                count += 1
                # same row
                for x in adjRow[curr[0]]:
                    if (curr[0], x) not in visited:
                        stack.append((curr[0], x))
                        visited.add((curr[0], x))
                # same column
                for y in adjCol[curr[1]]:
                    if (y, curr[1]) not in visited:
                        stack.append((y, curr[1]))
                        visited.add((y, curr[1]))

            return count

        result = 0
        for stone in stones:
            islandCells = dfs(*stone)
            if islandCells > 0:
                # for each "island" of cells connected by the
                # same row/column, remove all except 1
                result += islandCells - 1

        return result


if __name__ == "__main__":
    puzzles = [
        [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]],
        [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]],
        [[0, 0]]
    ]
    for puzzle in puzzles:
        print(Solution().removeStones(puzzle))
