# 884. Uncommon Words from Two Sentences

from utils import chunk
from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count1, count2 = Counter(s1.split(" ")), Counter(s2.split(" "))
        word1, word2 = set(count1), set(count2)

        # filter words that do not appear in the other sentene
        candidates = [*word1.difference(word2), *word2.difference(word1)]

        # check if word appears exactly once
        return [word for word in candidates if count1[word] == 1 or count2[word] == 1]


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "this apple is sweet",
        "this apple is sour",
        "apple apple",
        "banana"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().uncommonFromSentences(*puzzle))
