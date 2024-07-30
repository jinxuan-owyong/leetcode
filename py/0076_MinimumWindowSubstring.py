# 76. Minimum Window Substring

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""

        required = Counter(t)
        window = defaultdict(lambda: 0)

        # count refers to the number of groups of characters that the
        # requirement has been fulfilled (not number of characters!)
        currCount = 0
        requiredCount = len(required)
        substring = ""

        i = 0
        for j, ch in enumerate(s):
            if ch in required:
                window[ch] += 1

                # only update if all groups of characters is met
                if required[ch] == window[ch]:
                    currCount += 1

            while currCount == requiredCount:
                if window[ch] == required[ch] and (not substring or (j - i + 1) < len(substring)):
                    substring = s[i:j+1]

                if s[i] in required:
                    # if removal of s[i] results in the requirement being unmet
                    if required[s[i]] == window[s[i]]:
                        currCount -= 1
                    window[s[i]] -= 1

                i += 1

        return substring


if __name__ == "__main__":
    puzzles = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("aaaaaaaaaaaabbbbbcdd", "abcdd")
    ]
    for puzzle in puzzles:
        print(Solution().minWindow(*puzzle))

"""
Runtime
182
ms
Beats
23.59%
of users with Python3
Memory
17.30
MB
Beats
37.49%
of users with Python3
26*
"""
