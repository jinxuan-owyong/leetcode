# 2516. Take K of Each Character From Left and Right

from utils import chunk


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def idx(c):
            return ord(c) - ord('a')

        total = [0, 0, 0]  # a, b, c
        for c in s:
            total[idx(c)] += 1
        if any(map(lambda x: x < k, total)):
            return -1

        # goal: maximise the "middle" section to be removed to get the minimum minutes
        # remove as much as possible from the current window until the string is invalid
        largest = 0
        left = 0
        for right in range(len(s)):
            total[idx(s[right])] -= 1

            while min(total) < k:
                total[idx(s[left])] += 1
                left += 1

            largest = max(right - left + 1, largest)

        # left + right = total - middle
        return len(s) - largest


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "aabaaaacaabc", 2,
        "a", 1,
        "bbbbaccccb", 1,
        "abc", 0,
        "cacbcc", 1
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().takeCharacters(*puzzle))
