# 2381. Shifting Letters II

from utils import chunk
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        BACKWARD, FORWARD = 0, 1
        """
        use a single array to keep track of the start and end of the shifts in a character
        [start, end, direction] = [2, 4, 0]
        [0, 0, 0, 0, 0, 0] -> [0, 0, -1, 0, 1, 0]
        "1" denotes a forward shift, while "-1" denotes backward
        then we can keep track of the number of shifts with a counter during the final pass,
        adding or subtracting based on count[i]
        """
        change = [0] * (len(s)+1)
        for start, end, direction in shifts:
            change[start] += -1 if direction == BACKWARD else 1
            change[end+1] += 1 if direction == BACKWARD else -1

        result = []
        offset = 0
        for i in range(len(s)):
            offset += change[i]
            result.append(chr((ord(s[i]) - ord('a') + offset) % 26 + ord('a')))

        return ''.join(result)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "abc",
        [[0, 1, 0], [1, 2, 1], [0, 2, 1]],
        "dztz",
        [[0, 0, 0], [1, 1, 1]],
        "funny",
        [[0, 3, 0], [1, 4, 1], [2, 3, 1]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().shiftingLetters(*puzzle))
