# 1769. Minimum Number of Operations to Move All Balls to Each Box

from utils import chunk
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        goal: sum the distances of each ball from position i
        "110"
        dest  moves
          0   1 -> 0                 = 1
          1   0 -> 1                 = 1
          2   0 -> 1, 1 -> 2, 1 -> 2 = 3

        determine the prefix sum of ball distances to the left and right of position i
        for every step taken, the distance increases by the number of balls in the previous box,
        in addition to any ball from the previous step
        then at position i, the balls need to move left[i] + right[i] steps

                0     0     1     0     1     1 
        left    0     0     0     1     2     3+1
        right   5+4+2 4+3+1 3+2   2+1   1     0
        """

        left = [[0, 0] for _ in range(len(boxes))]  # num moves, num balls
        left[0][1] = int(boxes[0])
        for i in range(1, len(boxes)):
            prevMoves, prevBalls = left[i-1]
            left[i][0] = prevMoves + prevBalls
            left[i][1] = prevBalls + int(boxes[i])

        right = [[0, 0] for _ in range(len(boxes))]
        right[-1][1] = int(boxes[-1])
        for i in reversed(range(len(boxes) - 1)):
            prevMoves, prevBalls = right[i+1]
            right[i][0] = prevMoves + prevBalls
            right[i][1] = prevBalls + int(boxes[i])

        result = [0] * len(boxes)
        for i in range(len(boxes)):
            result[i] = left[i][0] + right[i][0]

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "110",
        "001011",
        "0",
        "1",
        "00",
        "01",
        "10",
        "11"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minOperations(*puzzle))
