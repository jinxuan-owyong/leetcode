# 1684. Count the Number of Consistent Strings

from utils import chunk
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        valid = set(allowed)
        for word in words:
            count += set(word).issubset(valid)
        return count


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "ab",
        ["ad", "bd", "aaab", "baa", "badab"],
        "abc",
        ["a", "b", "c", "ab", "ac", "bc", "abc"],
        "cad",
        ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"],
        "abc",
        ["a", "b", "c", "d", "ab", "ac", "bc", "abc", "abcd"]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countConsistentStrings(*puzzle))
