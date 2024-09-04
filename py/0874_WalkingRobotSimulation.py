# 874. Walking Robot Simulation

from utils import chunk
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        valid = set(map(tuple, obstacles))
        y, x = 0, 0

        # maps dy, dx to N E S W in clockwise direction
        curr = 0   # north
        result = 0  # max euclidean distance
        for command in commands:
            if command < 0:
                if command == -1:  # right
                    curr = (curr + 1) % 4
                else:
                    curr = curr - 1 if curr > 0 else 3
            else:
                dy, dx = DIRECTIONS[curr]
                steps = 0
                # traverse until out of steps or hit obstacle
                while steps < command and (x + dx, y + dy) not in valid:
                    x, y = x + dx, y + dy
                    result = max(result, x ** 2 + y ** 2)
                    steps += 1

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [4, -1, 3],
        [],
        [4, -1, 4, -2, 4],
        [[2, 4]],
        [6, -1, -1, 6],
        [],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().robotSim(*puzzle))
