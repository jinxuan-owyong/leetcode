# 62. Unique Paths

from utils import chunk


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        use a 2d array to keep track of the number of ways to reach a cell
        since the robot can only move down or right, it can only come from up or left
        the number of ways to reach a cell (i, j) is the sum of ways to reach cell (i-1, j) and (i, j-1)
        """
        # can be simplified to 1D since only previous row is used
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i-1 in range(m):
                    dp[i][j] += dp[i-1][j]
                if j-1 in range(n):
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        3, 7,
        3, 2,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().uniquePaths(*puzzle))
