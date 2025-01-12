# 678. Valid Parenthesis String

from utils import chunk


class Solution:
    def checkValidString(self, s: str) -> bool:
        # greedily match with open parenthesis, otherwise wildcard
        open, wildcard = [], []

        for i, paren in enumerate(s):
            match paren:
                case "(":
                    open.append(i)
                case "*":
                    wildcard.append(i)
                case ")":
                    if open:
                        open.pop()
                    elif wildcard:
                        wildcard.pop()
                    else:  # no "left" to match with "right"
                        return False

        # close remaining open parentheses with wildcard
        while open and wildcard and open[-1] < wildcard[-1]:
            open.pop()
            wildcard.pop()

        return len(open) == 0


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "()",
        "(*)",
        "(*))",
        "(()",
        "())",
        "***(((",
        "*)*)"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().checkValidString(*puzzle))
