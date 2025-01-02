# 2559. Count Vowel Strings in Ranges

from utils import chunk
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # prefix sum of vowel strings
        vowels = [0] * (len(words)+1)
        for i, word in enumerate(words):
            vowels[i+1] = vowels[i]
            if word[0] in "aeiou" and word[-1] in "aeiou":
                vowels[i+1] += 1

        result = [0] * len(queries)
        for i, (start, end) in enumerate(queries):
            result[i] = vowels[end+1] - vowels[start]

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        ["aba", "bcb", "ece", "aa", "e"],
        [[0, 2], [1, 4], [1, 1]],
        ["a", "e", "i"],
        [[0, 2], [0, 1], [2, 2]],
        ["aba"],
        [[0, 0]],
        ["abc"],
        [[0, 0]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().vowelStrings(*puzzle))
