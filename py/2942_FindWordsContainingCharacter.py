# 2942. Find Words Containing Character

from utils import chunk
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        ["leet", "code"],
        "e",
        ["abc", "bcd", "aaaa", "cbc"],
        "a",
        ["abc", "bcd", "aaaa", "cbc"],
        "z",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findWordsContaining(*puzzle))
