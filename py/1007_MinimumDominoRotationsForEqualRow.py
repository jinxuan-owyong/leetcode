# 1007. Minimum Domino Rotations For Equal Row

from utils import chunk
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        a number must be the majority half if it is a possible rotation
        find the majority then attempt to rotate the majority to the top row
        number of rotations required is len(row) - num majority in row
        rotation is not possible if both top and bottom do not have the majority element
        """
        N = len(tops)

        count = [0] * (6+1)
        for i in range(N):
            count[tops[i]] += 1
            count[bottoms[i]] += 1

        majority = 0
        for i in range(6+1):
            if count[i] >= N:  # N is half of total elements
                majority = i

        if not majority:
            return -1

        def getCount(keep, flip):
            rotations = 0
            for i in range(len(keep)):
                if keep[i] != majority:
                    if flip[i] != majority:
                        return -1
                    rotations += 1
            return rotations

        top, bot = getCount(tops, bottoms), getCount(bottoms, tops)
        if top < 0:
            return bot
        if bot < 0:
            return top
        return min(top, bot)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 1, 2, 4, 2, 2],
        [5, 2, 6, 2, 3, 2],
        [3, 5, 1, 2, 3],
        [3, 6, 3, 3, 4],
        [1, 2, 1, 1, 1, 2, 2, 2],
        [2, 1, 2, 2, 2, 2, 2, 2],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minDominoRotations(*puzzle))
