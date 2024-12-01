# 1346. Check If N and Its Double Exist

from utils import chunk
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        freq = {}
        for el in arr:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1

        for curr in arr:
            if curr == 0:
                if freq[0] > 1:
                    return True
            else:
                if curr * 2 in freq or (curr % 2 == 0 and curr // 2 in freq):
                    return True

        return False


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [10, 2, 5, 3],
        [3, 1, 7, 11],
        [0],
        [0, 1, 2, 0]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().checkIfExist(*puzzle))
