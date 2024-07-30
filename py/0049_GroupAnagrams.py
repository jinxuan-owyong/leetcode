# 49. Group Anagrams

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(lambda: [])
        for s in strs:
            anagrams[''.join(sorted(s))].append(s)
        return list(anagrams.values())


if __name__ == "__main__":
    puzzles = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"]
    ]
    for puzzle in puzzles:
        print(Solution().groupAnagrams(puzzle))

"""
Runtime
80
ms
Beats
92.43%
of users with Python3
Memory
19.60
MB
Beats
78.48%
of users with Python3
6
"""
