# 150. Evaluate Reverse Polish Notation

from utils import chunk
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            # perform floor division on absolute value, then restore negative sign if only either is negative
            # alternatively use int to truncate toward zero
            '/': lambda a, b: (-1 if (a < 0 and b >= 0 or a >= 0 and b < 0) else 1) * (abs(a)//abs(b)),
        }
        stack = []
        for t in tokens:
            if t in op:
                b, a = stack.pop(), stack.pop()
                res = op[t](a, b)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["2", "1", "+", "3", "*"],
        ["1", "2", "+", "3", "*", "4", "-"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().evalRPN(*puzzle))
