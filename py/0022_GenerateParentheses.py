# 22. Generate Parentheses

from utils import chunk
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        path = []

        def dfs(left, right):
            if left == 0 and right == 0:
                combinations.append(''.join(path))
                return
            if left > 0:
                path.append('(')
                dfs(left-1, right)
                path.pop()
            # we can only close the parenthesis when there is a matching open
            if right > 0 and left < right:
                path.append(')')
                dfs(left, right-1)
                path.pop()
        dfs(n, n)
        return combinations


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        1, 2, 3
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().generateParenthesis(*puzzle))
