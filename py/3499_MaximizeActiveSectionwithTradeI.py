# 3499. Maximize Active Section with Trade I

from utils import chunk


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # split s into blocks of '0's and '1's
        blocks = []
        i = 0
        for j in range(len(s)):
            if s[i] != s[j]:
                blocks.append(s[i:j])
                i = j
        blocks.append(s[i:])

        # check every "0..0", "1..1", "0..0" group
        # each 010 group adds on to the initial value of '1's
        ones = s.count('1')
        result = ones
        i = 0
        for i in range(len(blocks)-2):
            if blocks[i][0] == "0":
                # new flipped '0's become active
                result = max(ones + len(blocks[i]) + len(blocks[i+2]), result)

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "01",
        "0100",
        "1000100",
        "01010",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxActiveSectionsAfterTrade(*puzzle))
