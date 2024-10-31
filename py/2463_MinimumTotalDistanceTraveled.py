# 2463. Minimum Total Distance Traveled

from utils import chunk
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        slots = []
        for pos, count in factory:
            slots.extend([pos] * count)

        # memory limit exceeded
        # cache = {}
        memo = [[None] * len(slots) for _ in robot]
        # robot[i], slots[j]

        def helper(i: int, j: int):
            if i in range(len(robot)) and j in range(len(slots)) and memo[i][j]:
                return memo[i][j]
            if i == len(robot):
                return 0
            if j == len(slots):
                return float('inf')

            repair = helper(i + 1, j + 1) + abs(slots[j] - robot[i])
            skip = helper(i, j + 1)

            memo[i][j] = min(repair, skip)
            return min(repair, skip)

        return helper(0, 0)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [0, 4, 6],
        [[2, 2], [6, 2]],
        [1, -1],
        [[-2, 1], [2, 1]],
        [-3, 0, 1, 2, 3],
        [[-1, 5], [3, 1]],
        [-3, 0, 1, 2, 3],
        [[-1, 1], [3, 5]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumTotalDistance(*puzzle))
