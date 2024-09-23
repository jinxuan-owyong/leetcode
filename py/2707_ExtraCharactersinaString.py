# 2707. Extra Characters in a String

from utils import chunk
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        validWords = set(dictionary)
        cache = {}

        def dfs(i: int) -> int:
            if i in cache:
                return cache[i]

            if i == len(s):
                return 0

            # choice 1: find substring in dictionary
            res = float('inf')
            j = i
            while j < len(s):
                if s[i:j + 1] in validWords:
                    res = min(res, dfs(j + 1))
                j += 1

            # choice 2: skip the current character
            res = min(res, 1 + dfs(i + 1))

            cache[i] = res
            return res

        return dfs(0)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "leetscode",
        ["leet", "code", "leetcode"],
        "sayhelloworld",
        ["hello", "world"],
        "abcdefg",
        ["abc", "cdefg"]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minExtraChar(*puzzle))
