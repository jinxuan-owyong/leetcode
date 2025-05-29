# 139. Word Break

from utils import chunk
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom-up approach
        # dp[i] tells us whether we can form s[i:] with words from wordDict
        dp = [False] * (len(s)+1)
        dp[-1] = True

        for i in reversed(range(len(s))):
            for word in wordDict:
                end = i+len(word)
                if end <= len(s) and s[i:end] == word:
                    dp[i] = dp[end]
                    if dp[i]:
                        break

        return dp[0]

        # # top-down approach
        # cache = {}

        # def helper(i: int) -> bool:
        #     # we already checked s[i:], no need to repeat
        #     if i in cache:
        #         return cache[i]
        #     if i == len(s):
        #         return True

        #     for word in wordDict:
        #         # word is a prefix of s[i:]
        #         if s[i:i+len(word)] == word:
        #             if helper(i+len(word)):
        #                 return True

        #     cache[i] = False
        #     # no matching prefix
        #     return False

        # return helper(0)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "leetcode",
        ["leet", "code"],
        "applepenapple",
        ["apple", "pen"],
        "catsandog",
        ["cats", "dog", "sand", "and", "cat"],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().wordBreak(*puzzle))
