# 2326. Spiral Matrix IV

from typing import Optional, List
from classes import ListNode
from utils import chunk, toLinkedList


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1] * n for _ in range(m)]
        # upper, lower, left, right limits
        y1, y2, x1, x2 = 0, m - 1, 0, n - 1
        # right, down, left, up - [y, x]
        DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        curr = RIGHT if n > 1 else DOWN  # start with right
        y, x = 0, 0

        while head:
            dy, dx = DIRECTIONS[curr]
            result[y][x] = head.val
            y, x = y + dy, x + dx
            head = head.next

            # reduce matrix boundary if required
            isInRange = y + dy in range(y1, y2 + 1) and \
                x + dx in range(x1, x2 + 1)
            if not isInRange:
                if curr == RIGHT:
                    y1 += 1
                elif curr == DOWN:
                    x2 -= 1
                elif curr == LEFT:
                    y2 -= 1
                elif curr == UP:
                    x1 += 1
                # turn right
                curr = (curr + 1) % 4

        return result


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        3,
        5,
        [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0],
        1,
        4,
        [0, 1, 2],
        6,
        1,
        [2, 3, 4],
        3,
        2,
        [1, 2, 3, 4, 5]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().spiralMatrix(*puzzle[:2], toLinkedList(puzzle[2])))
