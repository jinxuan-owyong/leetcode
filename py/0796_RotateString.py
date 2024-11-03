# 796. Rotate String

from utils import chunk


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # since we can rotate s to form goal, then concatenating s to itself
        # gives us abcdeabcde. all 5 possible rotations are substrings of 2s
        # hence we check if goal is a substring of 2s
        return goal in s + s


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "abcde", "cdeab",
        "abcde", "abced",
        "eabcd", "abcde",
        "ab", "abc",
        "a", "b",
        "a", "a",
        "aa", "a",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().rotateString(*puzzle))
