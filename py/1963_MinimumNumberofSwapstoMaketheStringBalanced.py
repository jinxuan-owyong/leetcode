# 1963. Minimum Number of Swaps to Make the String Balanced

from utils import chunk


class Solution:
    def minSwaps(self, s: str) -> int:
        curr = 0  # [ = -1 and ] = 1
        result = 0  # the largest curr = how many pairs out of order
        for b in s:
            match b:
                case '[':
                    curr -= 1
                case ']':
                    curr += 1
            result = max(curr, result)

        # each ] swap reduces the number of out of order brackets by 2
        return (result + 1) // 2


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "][][",
        "]]][[[",
        "[]",
        "[][[]][]",
        ']][][][[',
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minSwaps(*puzzle))
