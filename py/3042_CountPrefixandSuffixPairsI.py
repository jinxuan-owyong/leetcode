# 3042. Count Prefix and Suffix Pairs I

from utils import chunk
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    result += 1

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["a", "aba", "ababa", "aa"],
        ["pa", "papa", "ma", "mama"],
        ["abab", "ab"],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countPrefixSuffixPairs(*puzzle))
