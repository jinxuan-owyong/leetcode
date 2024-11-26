# 2924. Find Champion II

from utils import chunk
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        """
        use a bitmask to keep track of nodes that do not have a stronger node
        initially assume all to be the strongest
        clear that bit if another edge points to it
        """

        withoutParent = 2 ** n - 1

        for _, v in edges:
            withoutParent &= ~(1 << v)

        result = -1
        i = 0
        for i in range(100):
            if withoutParent & 1:
                if result >= 0:
                    return -1
                result = i
            withoutParent >>= 1

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        3, [[0, 1], [1, 2]],
        4, [[0, 2], [1, 3], [1, 2]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findChampion(*puzzle))
