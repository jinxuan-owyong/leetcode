# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        curr, temp = n, 0
        seen = set()
        while True:
            if curr == 1:
                return True
            if curr in seen:
                return False
            seen.add(curr)
            for d in str(curr):
                temp += int(d) ** 2
            curr, temp = temp, 0


if __name__ == "__main__":
    puzzles = [19, 2, 1, 2147483647]
    for puzzle in puzzles:
        print(Solution().isHappy(puzzle))

"""
Runtime
32
ms
Beats
84.73%
of users with Python3
Memory
16.50
MB
Beats
80.61%
of users with Python3
6
"""
