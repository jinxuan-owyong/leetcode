# 3223. Minimum Length of String After Operations

from utils import chunk
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        """
        for any character, there will be at most 2 remaining after removal
        if there are 1 or 2 counts, then they will not be changed
        suppose we have "aaaaaaaa". we keep deleting indexes 0 and 2 until we are left with "aa"
        any odd number of characters will reduce to 1, even to 2
        """

        freq = Counter(s)
        result = 0

        for c in freq:
            result += 2 if freq[c] % 2 == 0 else 1

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "abaacbcbb",
        "aa",
        "aaaaaaaa"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumLength(*puzzle))
