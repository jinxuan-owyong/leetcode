# 1371. Find the Longest Substring Containing Vowels in Even Counts

from utils import chunk


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a": 4, "e": 3, "i": 2, "o": 1, "u": 0}
        # calculate prefix xor of vowel mask
        curr = 0
        first = {}
        result = ""
        for i, c in enumerate(s):
            if c in vowels:
                curr ^= 1 << vowels[c]

            # first occurrence of prefix xor
            if curr not in first:
                first[curr] = i

            # substring is even from first word
            if curr == 0:
                # any substring here is longer than all previous strings
                result = s[:i + 1]

            # take first[curr] == masks[j-1] matching curr
            # the resulting substring s[j:i+1] has no/even vowels
            else:
                j = first[curr] + 1
                if i - j + 1 > len(result):
                    result = s[j:i + 1]

        print(result, end=': ')
        return len(result)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "eleetminicoworoep",
        "leetcodeisgreat",
        "bcbcbc",
        "abcdefgfedcba",
        "abbaabbb",
        "aaaa",
        "a",
        "b",
        "ba",
        "babebbbb"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findTheLongestSubstring(*puzzle))
