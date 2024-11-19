# 1652. Defuse the Bomb

from utils import chunk
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        code.extend(code)
        window = sum(code[1:k+1]) if k > 0 else sum(code[k:])
        # i, j point to the start and end of the current window
        i, j = (1, k) if k > 0 else (k, -1)

        result = []
        for _ in range(len(code) // 2):
            result.append(window)
            # slide window to the right by 1
            window += code[j + 1] - code[i]
            i, j = i + 1, j + 1

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [5, 7, 1, 4], 3,
        [1, 2, 3, 4], 0,
        [2, 4, 9, 3], -2,
        [5, 7, 1, 4], -1,
        [2, 3], 1
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().decrypt(*puzzle))
