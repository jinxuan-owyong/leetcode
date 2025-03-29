# 3498. Reverse Degree of a String

from utils import chunk


class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = {ch: 26 - (ch - ord('a')) for ch in range(ord('a'), ord('a')+26)}
        return sum(degree[ord(c)] * (i + 1) for i, c in enumerate(s))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "abc",
        "zaza",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().reverseDegree(*puzzle))
