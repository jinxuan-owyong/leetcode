# 2131. Longest Palindrome by Concatenating Two Letter Words

from utils import chunk
from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        # the middle word can only be a palindrome with odd count, or none if it doesn't exist
        middle = ""
        # only add words if their flipped counterparts exist in words
        # then we can flip "left" and add to the middle
        left = ""
        # repeated words can be added to the left and right of the middle word
        repeated = ""

        added = set()
        for c in count:
            flipped = c[::-1]
            if c == flipped:
                repeated += c * (count[c] // 2)
                if count[c] % 2 == 1:
                    middle = c
            elif flipped in count and c not in added:
                left += c * count[c]
                added.add(c)
                added.add(flipped)

        return len(middle) + (2 * len(repeated)) + (2 * len(left))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["lc", "cl", "gg"],
        ["ab", "ty", "yt", "lc", "cl", "ab"],
        ["cc", "ll", "xx"],
        ["dd", "aa", "bb", "dd", "aa", "dd", "bb",
            "dd", "aa", "cc", "bb", "cc", "dd", "cc"],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().longestPalindrome(*puzzle))
