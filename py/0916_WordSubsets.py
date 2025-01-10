# 916. Word Subsets

from utils import chunk
from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # we only care about the maximum count required for each character a-z
        required = {}
        for word in words2:
            curr = Counter(word)
            for k in curr:
                if k in required:
                    required[k] = max(required[k], curr[k])
                else:
                    required[k] = curr[k]

        result = []
        for curr in words1:
            word = Counter(curr)
            # a string is a subset of all the strings in words2 if the character count in required is met
            if all([word[k] >= required[k] for k in required]):
                result.append(curr)

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        ["amazon", "apple", "facebook", "google", "leetcode"],
        ["e", "o"],
        ["amazon", "apple", "facebook", "google", "leetcode"],
        ["l", "e"],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().wordSubsets(*puzzle))
