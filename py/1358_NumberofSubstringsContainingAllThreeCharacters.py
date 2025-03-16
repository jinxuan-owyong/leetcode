# 1358. Number of Substrings Containing All Three Characters

from utils import chunk


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        use sliding window to find windows containing abc
        for each valid window, we can add characters to the back to get substrings
        shrink window only if it is valid. a window can contain valid sub-windows, so add substrings during shrinking as well
        """
        window = {"a": 0, "b": 0, "c": 0}
        result = 0
        i = 0

        for j in range(len(s)):
            window[s[j]] += 1

            while window["a"] and window["b"] and window["c"]:
                window[s[i]] -= 1
                i += 1
                result += len(s) - j

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "abcabc",
        "aaacb",
        "abc",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().numberOfSubstrings(*puzzle))
