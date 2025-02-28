# 76. Minimum Window Substring

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""

        required = Counter(t)
        window = {}
        # number of characters in window that fulfil window[ch] >= required[ch]
        curr = 0

        result = ""
        resultLength = float("inf")

        i = 0
        for j in range(len(s)):
            window[s[j]] = window.get(s[j], 0) + 1

            if window[s[j]] == required[s[j]]:
                curr += 1  # this will only be incremented once when the character meets the requirement

            if curr == len(required):
                # if beginning of window is irrelevant
                while i < j and window[s[i]] > required[s[i]]:
                    window[s[i]] -= 1
                    i += 1

                if j-i+1 < resultLength:
                    result, resultLength = s[i:j+1], j-i+1

                # when the window meets the substring requirements, then there is no incentive to
                # futher grow the window. instead, shrink the window until it is invalid
                while i < j and curr == len(required):
                    window[s[i]] -= 1
                    if s[i] in required and window[s[i]] < required[s[i]]:
                        curr -= 1
                    i += 1

        return result


if __name__ == "__main__":
    puzzles = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("ab", "b"),
        ("aaaaaaaaaaaabbbbbcdd", "abcdd")
    ]
    for puzzle in puzzles:
        print(Solution().minWindow(*puzzle))
