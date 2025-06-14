# 202. Happy Number

from utils import chunk


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 1 and n not in visited:
            visited.add(n)
            # alternatively use %10 and //= 10 on a temporary variable
            n = sum(map(lambda x: int(x)**2, str(n)))
        return n == 1


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        19, 2, 100, 101
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().isHappy(*puzzle))
