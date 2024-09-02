# 1894. Find the Student that Will Replace the Chalk

from utils import chunk
from typing import List
import bisect


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefixSum = [0] * len(chalk)
        prefixSum[0] = chalk[0]
        for i in range(1, len(chalk)):
            prefixSum[i] = prefixSum[i - 1] + chalk[i]

        # pass the chalk until it is the final round
        k = k % sum(chalk)

        # if k == 0, the last student used up all the chalk, but does not have to replace
        # perform binary search to determine when the chalk is depleted
        # k < sum(chalk), i will be within index range
        i = bisect.bisect_left(prefixSum, k)
        if prefixSum[i] == k:
            i += 1
        return i


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [5, 1, 5],
        22,
        [3, 4, 1, 2],
        25,
        [1, 2, 3, 4],
        9,
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        9
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().chalkReplacer(*puzzle))
