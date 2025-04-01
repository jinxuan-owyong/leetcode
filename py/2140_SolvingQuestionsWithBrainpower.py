# 2140. Solving Questions With Brainpower

from utils import chunk
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        build dp array from back to front
        dp[i] holds the best possible score whether it was skipped or answered previously

        compare the points from taking the larger of 
        - dp[i+1] (skip) or 
        - points + dp[i+brainpower+1] (answer)
        since we skip over brainpower[i] questions, then we take the last valid score, which is from the (i+brainpower+1)th index
        """

        N = len(questions)
        dp = [0] * N
        dp[-1] = questions[-1][0]

        for i in reversed(range(N-1)):
            points, brainpower = questions[i]
            nextQn = dp[i+brainpower+1] if i+brainpower+1 < N else 0
            dp[i] = max(dp[i+1], points + nextQn)

        return dp[0]


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[3, 2], [4, 3], [4, 4], [2, 5]],
        [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().mostPoints(*puzzle))
