# 76. Minimum Window Substring

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        keep track of number of matched characters when expanding the window
        each time all characters match, we shrink the window until the window is invalid

        OUZODYXAZV 
        -> OUZODYX expand
        ->    ODYX shrink further
        -> ODYXAZ  expand
        ->   YXAZ  shrink
        """
        if len(s) < len(t):
            return ""

        required = Counter(t)
        window = defaultdict(int)
        matches = 0  # number of window[c] >= required[c]

        i = 0
        result = ""
        for j in range(len(s)):
            window[s[j]] += 1
            # as we expand the window, we will "pass by" the required value only once
            # then keep track of number of characters that match the count to avoid repeated work
            if window[s[j]] == required[s[j]]:
                matches += 1

            # expand window until we have all matching characters
            while i <= j and matches == len(required):
                # as we shrink the window, keep track of the shortest substring
                # invariant: s[i:j+1] meets the character requirement of t
                if not result or j-i+1 < len(result):
                    result = s[i:j+1]
                if window[s[i]] == required[s[i]]:
                    matches -= 1
                window[s[i]] -= 1
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
