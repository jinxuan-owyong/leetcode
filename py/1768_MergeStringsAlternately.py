# 1768. Merge Strings Alternately

from utils import chunk


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        i = 0
        while i < len(word1) and i < len(word2):
            result += word1[i]
            result += word2[i]
            i += 1

        # at most 1 statement will be true
        if i < len(word1):
            result += word1[i:]
        if i < len(word2):
            result += word2[i:]

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "abc",
        "pqr",
        "ab",
        "pqrs",
        "abcd",
        "pq",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().mergeAlternately(*puzzle))
