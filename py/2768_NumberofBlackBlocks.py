# 2768. Number of Black Blocks

from utils import chunk
from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        blacks = defaultdict(int)

        for i, j in coordinates:
            # mark the possible matrices that the black cell can fall into
            # using the top left (i+dy, j+dx) to identify a 2x2 matrix
            DIRS = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
            for dy, dx in DIRS:
                if i+dy in range(m-1) and j+dx in range(n-1):
                    blacks[(i+dy, j+dx)] += 1

        count = Counter(blacks.values())
        result = [count[i] for i in range(5)]
        result[0] = (m-1)*(n-1) - sum(result)

        return result


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        3, 3, [[0, 0]],
        3, 3, [[0, 0], [1, 1], [0, 2]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countBlackBlocks(*puzzle))
