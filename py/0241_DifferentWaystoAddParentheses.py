# 241. Different Ways to Add Parentheses

from utils import chunk
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def getOperatorFn(i: int):
            match expression[i]:
                case "+":
                    return lambda a, b: a + b
                case "-":
                    return lambda a, b: a - b
                case "*":
                    return lambda a, b: a * b

        def getPossibilities(group1: List[int], group2: List[int], operand: int) -> List[int]:
            result = []
            fn = getOperatorFn(operand)
            for a in group1:
                for b in group2:
                    result.append(fn(a, b))
            return result

        def helper(left: int, right: int) -> List[int]:
            curr = []

            # split expression at the operator
            for i in range(left, right + 1):
                if expression[i] in "+-*":
                    group1 = helper(left, i - 1)
                    group2 = helper(i + 1, right)
                    # calculate possibilities based on result
                    curr.extend(getPossibilities(group1, group2, i))

            # no operands exist, hence we have an integer
            if not curr:
                curr.append(int(expression[left:right + 1]))

            return curr

        return helper(0, len(expression) - 1)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "2-1-1",
        "2*3-4*5"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().diffWaysToCompute(*puzzle))
