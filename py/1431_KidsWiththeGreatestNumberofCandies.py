# 1431. Kids With the Greatest Number of Candies

from utils import chunk
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        result = [False] * len(candies)
        for i in range(len(candies)):
            result[i] = (candies[i] + extraCandies) >= highest
        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [2, 3, 5, 1, 3],
        3,
        [4, 2, 1, 1, 2],
        1,
        [12, 1, 12],
        10,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().kidsWithCandies(*puzzle))
