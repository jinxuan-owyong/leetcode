# 773. Sliding Puzzle

from utils import chunk
from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        since the board is only 2x3, we can serialise the board with a string
        [[1, 2, 3], [4, 5, 0]] = "123450"
        this string can then be used to keep track of whether this pattern (node)
        has been seen before. as such, we can perform BFS on the valid next moves
        and the first occurrence of "123450" is the shortest path

        indices to identify the next move
        0 1 2
        3 4 5
        """

        nextMove = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4),
            4: (1, 3, 5),
            5: (2, 4)
        }
        start = ""
        for row in board:
            for cell in row:
                start += str(cell)

        visited = set()
        queue = deque([(start, 0, start.index('0'))])  # board, dist, zeroIdx

        def swapChars(s: str, i: int, j: int) -> str:
            a = list(s)
            a[i], a[j] = a[j], a[i]
            return ''.join(a)

        while queue:
            curr, dist, zeroIdx = queue.popleft()
            if curr == "123450":
                return dist
            elif curr in visited:
                continue
            visited.add(curr)
            for move in nextMove[zeroIdx]:
                queue.append((swapChars(curr, zeroIdx, move), dist + 1, move))

        return -1


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 2, 3], [4, 0, 5]],
        [[1, 2, 3], [5, 4, 0]],
        [[4, 1, 2], [5, 0, 3]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().slidingPuzzle(*puzzle))
