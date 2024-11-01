# 1957. Delete Characters to Make Fancy String

from utils import chunk


class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        i = 0

        while i < len(s):
            j = i
            # find >= 3 consecutive characters
            while j < len(s) - 2 and s[j] == s[j + 1] == s[j + 2]:
                j += 1

            # retain the first 2 chars if string is same
            result += s[i] * (1 if i == j else 2)

            # skip remaining consecutive characters, if any
            i = j + 1 if i == j else j + 2

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "leeetcode",
        "aaabaaaa",
        "aab",
        "yyyyummy",
        "yummm",
        "a",
        "ab",
        "aa",
        "aaaa"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().makeFancyString(*puzzle))
