# 1422. Maximum Score After Splitting a String

from utils import chunk


class Solution:
    def maxScore(self, s: str) -> int:
        """
        goal: maximise '0's on the left and '1's on the right
        use a hashmap to keep track of count of '0's and '1's
        """
        left = {'0': 0, '1': 0}
        right = {'0': 0, '1': 0}
        for c in s:
            right[c] += 1

        result = 0
        for i, c in enumerate(s):
            if i < len(s) - 1:
                left[c] += 1
                right[c] -= 1
                if (curr := left['0'] + right['1']) > result:
                    result = curr

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "011101",
        "00111",
        "1111",
        "00",
        "01",
        "10",
        "11"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxScore(*puzzle))
