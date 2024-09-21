# 386. Lexicographical Numbers

from utils import chunk
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def helper(prefix: int):
            for i in range(10):
                nextVal = prefix * 10 + i
                if nextVal > 0 and nextVal <= n:
                    result.append(nextVal)
                    helper(nextVal)

        helper(0)
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        13,
        2,
        9,
        33,
        1
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().lexicalOrder(*puzzle))
