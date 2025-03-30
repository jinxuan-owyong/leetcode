# 763. Partition Labels

from utils import chunk
from typing import List
from collections import Counter
from collections import defaultdict


class Solution:
    # counting
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        parts = []
        i = 0
        window = defaultdict(int)
        for j in range(len(s)):  # O(N)
            window[s[j]] += 1
            can = True
            for ch in window:  # O(26)
                can = can and window[ch] == count[ch]
            if can:
                parts.append(j-i+1)
                window.clear()
                i = j+1
        return parts


# class Solution:
#     # intervals
#     def partitionLabels(self, s: str) -> List[int]:
#         """
#         find partitions containing start and end of a character
#         merge 26 intervals and return their width
#         """
#         intervals = [[float('inf'), 0] for _ in range(26)]
#         for i, c in enumerate(s):
#             curr = ord(c)-97
#             left, right = intervals[curr]
#             intervals[curr][0] = min(i, intervals[curr][0])
#             intervals[curr][1] = max(i, intervals[curr][1])

#         intervals.sort()
#         result = []
#         prev = intervals[0]
#         for i in range(1, 26):
#             curr = intervals[i]
#             if curr[0] < float('inf'):  # valid char in s
#                 # merge intervals
#                 if prev[1] >= curr[0]:
#                     prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
#                 else:
#                     # append partition width instead of interval
#                     result.append(prev[1]-prev[0]+1)
#                     prev = curr

#         result.append(prev[1]-prev[0]+1)
#         return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "ababcbacadefegdehijhklij",
        "eccbbbbdec",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().partitionLabels(*puzzle))
