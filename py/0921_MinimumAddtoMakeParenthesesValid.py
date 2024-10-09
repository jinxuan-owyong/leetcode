# 921. Minimum Add to Make Parentheses Valid

from utils import chunk


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        result = 0

        for b in s:
            if b == '(':
                stack.append(b)
            else:
                # '', '))'
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    result += 1

        # if stack is left with '((()'
        while stack and stack[-1] == ')':
            stack.pop()
            stack.pop()

        # stack is at most '(('
        return result + len(stack)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "())",
        "(((",
        "))((",
        "(((()))))))",
        "((((((())))",
        "(",
        ")",
        ")("
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minAddToMakeValid(*puzzle))
