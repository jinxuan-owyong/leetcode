# 791. Custom Sort String


from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordering = defaultdict(lambda: -1, {c: i for i, c in enumerate(order)})
        return "".join(sorted(s, key=lambda x: ordering[x]))


if __name__ == "__main__":
    puzzles = [
        ("cba", "abcd"),
        ("bcafg", "abcd")
    ]
    for puzzle in puzzles:
        print(Solution().customSortString(*puzzle))

"""
Runtime
39
ms
Beats
27.20%
Memory
16.60
MB
Beats
31.01%
"""
