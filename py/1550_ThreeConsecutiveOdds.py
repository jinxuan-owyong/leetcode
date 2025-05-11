# 1550. Three Consecutive Odds

from utils import chunk
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0
        for n in arr:
            if n % 2:
                odd += 1
                if odd == 3:
                    return True
            else:
                odd = 0
        return False


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 6, 4, 1],
        [1, 2, 34, 3, 4, 5, 7, 23, 12]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().threeConsecutiveOdds(*puzzle))
