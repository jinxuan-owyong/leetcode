# 1400. Construct K Palindrome Strings

from utils import chunk
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        N = len(s)
        if N < k:
            return False
        if N == 1 or N == k:
            return True

        """
        to form a palindrome, there should be at most 1 character with an odd count
        given "aabcdeee", there are 4 characters with an odd count
        - it is not possible to form 2 or 3 palindromes
        - we can form 4 palindromes: "aba", "c", "ede", "e"
        """

        freq = Counter(s)
        odd = sum(map(lambda x: freq[x] % 2, freq))
        return odd <= k


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "annabelle", 2,
        "leetcode", 3,
        "true", 4,
        "leetcode", 4,
        "false", 6
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().canConstruct(*puzzle))
