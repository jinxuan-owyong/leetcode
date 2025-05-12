# 2094. Finding 3-Digit Even Numbers

from utils import chunk
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = [0] * 10
        for d in digits:
            count[d] += 1

        result = []
        # check all 3 digit even numbers without leading zeros if it can be formed
        for i in range(100, 1000, 2):
            curr = [0] * 10
            temp = i
            while temp > 0:
                curr[temp % 10] += 1
                temp //= 10
            # digits required to form i must be available
            valid = True
            for d, freq in enumerate(curr):
                valid = valid and count[d] >= freq
            if valid:
                result.append(i)

        # already in sorted order since we enumerate from 100 to 1000
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 1, 3, 0],
        [2, 2, 8, 8, 2],
        [3, 7, 5],
        [4, 7, 4, 0, 3, 3, 6, 5, 0, 5, 7, 8, 0, 2, 9, 2, 3, 1, 8]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findEvenNumbers(*puzzle))
