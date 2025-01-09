# 2185. Counting Words With a Given Prefix

from utils import chunk
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        ["pay", "attention", "practice", "attend"],
        "at",
        ["leetcode", "win", "loops", "success"],
        "code"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().prefixCount(*puzzle))
