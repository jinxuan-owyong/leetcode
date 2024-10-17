# 670. Maximum Swap

from utils import chunk


class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        maxNum = -1
        # positions to be swapped
        i, j = -1, -1

        for k in reversed(range(len(s))):
            if maxNum == -1 or s[k] > s[maxNum]:
                maxNum = k
            elif s[k] < s[maxNum]:
                i = k
                j = maxNum
            
        if i >= 0 and j >= 0:
            s[i], s[j] = s[j], s[i]

        return int(''.join(s))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        2736,
        9973,
        4321,
        1234,
        1331,
        5324,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maximumSwap(*puzzle))
