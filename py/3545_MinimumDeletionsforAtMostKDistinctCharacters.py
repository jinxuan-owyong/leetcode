# 3545. Minimum Deletions for At Most K Distinct Characters

from utils import chunk
from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = Counter(s)
        if len(count) <= k:
            return 0
        # greedily delete the least frequently occurring characters
        order = sorted(count.items(), key=lambda x: x[1])
        deletions = 0
        for i, (ch, freq) in enumerate(order):
            deletions += freq
            if len(count)-(i+1) == k:
                break
        return deletions


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "abc", 2,
        "aabb", 2,
        "yyyzz", 1,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minDeletion(*puzzle))
