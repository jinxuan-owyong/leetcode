# 1653. Minimum Deletions to Make String Balanced


from collections import Counter
from collections import defaultdict


class Solution:
    def minimumDeletions(self, s: str) -> int:
        countLeft = defaultdict(lambda: 0)
        countRight = defaultdict(lambda: 0, Counter(s))
        deletions = 1E10

        # before mid = all "a"s
        # mid onwards = all "b"s
        for mid in s:
            deletions = min(deletions, countLeft["b"] + countRight["a"])
            countLeft[mid] += 1
            countRight[mid] -= 1

        # check the last position - if all "a"s
        return min(deletions, countLeft["b"] + countRight["a"])


if __name__ == "__main__":
    puzzles = [
        "aababbab",
        "bbaaaaabb",
        "bbbbb",
        "bbbbbaaaa",
        "bbaaaaaa",
        "a"
        "ab",
        "baba",
    ]
    for puzzle in puzzles:
        print(Solution().minimumDeletions(puzzle))

"""
Runtime
777
ms
Beats
11.67%
Memory
17.96
MB
Beats
40.00%
"""

# TLE
# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         stack = [(0, 0, False)]  # idx, cost, hasB
#         result = 1E10

#         while stack:
#             i, cost, hasB = stack.pop()

#             # drop all subsequent "a"s since we want a balanced string
#             if hasB:
#                 while i != len(s):
#                     if s[i] == "a":
#                         cost += 1
#                     i += 1

#             if i == len(s):
#                 result = min(result, cost)
#                 continue

#             if s[i] == "a":
#                 while i < len(s) and s[i] == "a":
#                     i += 1
#                 stack.append((i, cost, False))
#             else:
#                 stack.append((i + 1, cost, True))
#                 # skip the "b"s
#                 while i < len(s) and s[i] == "b":
#                     i += 1
#                     cost += 1
#                 stack.append((i, cost, False))

#         return result
