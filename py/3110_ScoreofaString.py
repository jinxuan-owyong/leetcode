# 3110. Score of a String


class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i in range(1, len(s)):
            result += abs(ord(s[i - 1]) - ord(s[i]))
        return result


if __name__ == "__main__":
    puzzles = [
        "hello",
        "zaz",
        "az"
    ]
    for puzzle in puzzles:
        print(Solution().scoreOfString(puzzle))

"""
Runtime
41
ms
Beats
23.86%
Memory
16.34
MB
Beats
90.06%
"""
