# 1106. Parsing A Boolean Expression
# https://leetcode.com/problems/parsing-a-boolean-expression/solutions/5942501/beats-100-0-python-stack-step-by-step-explanation/

from utils import chunk


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        parse = {
            "!": lambda s: "f" if s == "t" else "t",
            "&": lambda s: "t" if not "f" in s else "f",
            "|": lambda s: "t" if "t" in s else "f"
        }

        stack = []
        for c in expression:
            if c in "!&|tf":
                stack.append(c)
            elif c == ")":
                value = ""
                while stack[-1] not in "!&|":
                    value += stack.pop()
                operator = stack.pop()
                result = parse[operator](value)
                stack.append(result)

        return stack[0] == "t"


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "&(|(f))",
        "|(f,f,f,t)",
        "!(&(f,t))",
        "&(f)",
        "|(t)",
        "!(f)",
        "|(&(!(t),!(f)),t)",
        "&(t,t,!(f),|(f,t,t,f,f))",
        "!(!(|(&(!(&(|(!(&(|(!(&(|(t,f,f,t)))))))))))))"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().parseBoolExpr(*puzzle))
