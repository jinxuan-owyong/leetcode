# 1823. Find the Winner of the Circular Game

from utils import chunk
from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1, n + 1))

        while len(queue) > 1:
            # perform k - 1 rotations to the left
            # the person at the start is the kth to be removed
            queue.rotate(-(k - 1))
            queue.popleft()

        return queue[0]


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        5,
        2,
        6,
        5
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findTheWinner(*puzzle))
