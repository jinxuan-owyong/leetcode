# 2938. Separate Black and White Balls

from utils import chunk


class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        we don't actually need to shift, but instead count distance (j - i)
        shift '1' at position i all the way to position j
        1 1 0 0 1 0 
        ^i        ^j

        increment i until we reach a 1
        decrement j until we reach a 0
        0 1 0 0 1 1
          ^i  ^j

        stop if i >= j
        0 0 0 1 1 1
            ^j^i
        """
        i, j = 0, len(s) - 1
        steps = 0

        while i < j:
            while i < len(s) and s[i] == '0':
                i += 1

            while j >= 0 and s[j] == '1':
                j -= 1

            steps += j - i if j > i else 0
            i += 1
            j -= 1

        return steps


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "101",
        "100",
        "0111",
        "110011",
        "110010"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumSteps(*puzzle))
