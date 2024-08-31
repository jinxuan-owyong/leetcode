# 1021. Remove Outermost Parentheses


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []

        for c in s:
            if not stack:
                # first outer is removed
                stack.append(c)
                continue

            if c == ')':
                # all except last outer is part of result
                if len(stack) > 1:
                    result.append(c)
                stack.pop()
            else:
                stack.append(c)
                result.append(c)

        return "".join(result)


if __name__ == "__main__":
    puzzles = [
        "(()())(())",
        "(()())(())(()(()))",
        "()()"
    ]
    for puzzle in puzzles:
        print(Solution().removeOuterParentheses(puzzle))
