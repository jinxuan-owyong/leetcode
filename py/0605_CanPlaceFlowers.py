# 605. Can Place Flowers

from utils import chunk
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        # greedily plant flowers by checking if adjacent plots are empty
        planted = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and \
                (i == 0 or flowerbed[i-1] == 0) and \
                    (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                planted += 1
                if planted == n:
                    return True

        return False


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 0, 0, 0, 1],
        1,
        [1, 0, 0, 0, 1],
        2,
        [0, 0, 1, 0, 0],
        1,
        [1, 0, 1, 0, 1, 0, 1],
        0,

    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().canPlaceFlowers(*puzzle))
