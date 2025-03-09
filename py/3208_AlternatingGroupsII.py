# 3208. Alternating Groups II

from utils import chunk
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        3 <= k <= n <= 10^5
        brute force: check a k-sized window if it is has potentially an alternating group - both red and blue exists = O((n-k)*k)
        improvement: invalidate the whole window if there is a repeated colour
        """
        groups = 0
        alternating = 0  # number of alternating colours in window
        for i in range(len(colors)+k-1):
            if colors[(i-1) % len(colors)] == colors[i % len(colors)]:
                alternating = 1  # invalidate window
            else:
                alternating += 1
                # allow number of alternating groups can exceed k since we only care about the most recent k colours
                if alternating >= k:
                    groups += 1

        return groups


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [0, 1, 0, 1, 0],
        3,
        [0, 1, 0, 0, 1, 0, 1],
        6,
        [1, 1, 0, 1],
        4,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().numberOfAlternatingGroups(*puzzle))
