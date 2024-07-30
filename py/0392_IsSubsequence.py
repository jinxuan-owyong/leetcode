# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)


if __name__ == "__main__":
    puzzles = [
        ("abc", "ahbgdc"),
        ("axc", "ahbgdc")
    ]
    for puzzle in puzzles:
        print(Solution().isSubsequence(*puzzle))

"""
Runtime
34
ms
Beats
71.43%
of users with Python3
Memory
16.70
MB
Beats
39.92%
of users with Python3
6
"""
