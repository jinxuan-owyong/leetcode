# 2914. Minimum Number of Changes to Make Binary String Beautiful

from utils import chunk


class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                count += 1
        return count


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "1001",
        "10",
        "0000",
        "101010",
        "11101110"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minChanges(*puzzle))
