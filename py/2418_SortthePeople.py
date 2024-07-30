# 2418. Sort the People

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        order = sorted(enumerate(heights), key=lambda x: x[1], reverse=True)
        return [names[i] for i, _ in order]


if __name__ == "__main__":
    puzzles = [
        (["Mary", "John", "Emma"], [180, 165, 170]),
        (["Alice", "Bob", "Bob"], [155, 185, 150])
    ]
    for puzzle in puzzles:
        print(Solution().sortPeople(*puzzle))


"""
Runtime
106
ms
Beats
52.59%
Memory
16.92
MB
Beats
84.16%
"""
