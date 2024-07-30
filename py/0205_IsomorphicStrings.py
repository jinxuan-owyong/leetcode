# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # first 2 checks verify whether the strings are 1 - 1 mappable
        # if there are more characters in either sets, then this fails
        # set(zip(s, t)) gives us the unique mappings for s and t
        # if there are more mappings than unique characters in s and t,
        # then the string is not isomorphic
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


if __name__ == "__main__":
    puzzles = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
        ("bbbaaaba", "aaabbbba"),
        ("badc", "baba")
    ]
    for puzzle in puzzles:
        print(Solution().isIsomorphic(*puzzle))

"""
Runtime
33
ms
Beats
94.25%
of users with Python3
Memory
16.68
MB
Beats
94.17%
of users with Python3
18*
"""
