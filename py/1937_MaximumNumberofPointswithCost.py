# 1937. Maximum Number of Points with Cost

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # keep track of points so far at curr[i], the next move to take
        curr = points[0].copy()

        # at each row, we pre-determine the best element from the left/right
        for i in range(len(points) - 1):
            dpLeft = [curr[0]] * len(curr)
            dpRight = [curr[-1]] * len(curr)

            # take either the curernt position or the neighbour
            for j in range(1, len(dpLeft)):
                dpLeft[j] = max(dpLeft[j - 1] - 1, curr[j])
            for j in reversed(range(len(dpLeft) - 1)):
                dpRight[j] = max(dpRight[j + 1] - 1, curr[j])

            # take step for curr from row i to i + 1
            curr = points[i + 1].copy()
            for j in range(len(curr)):
                curr[j] += max(dpLeft[j], dpRight[j])

        return max(curr)


if __name__ == "__main__":
    puzzles = [
        [[1, 2, 3], [1, 5, 1], [3, 1, 1]],
        [[1, 5], [2, 3], [4, 2]]
    ]
    for puzzle in puzzles:
        print(Solution().maxPoints(puzzle))
