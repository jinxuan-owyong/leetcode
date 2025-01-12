# 2116. Check if a Parentheses String Can Be Valid

from utils import chunk


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        open, wildcard = [], []
        for i, (paren, lock) in enumerate(zip(s, locked)):
            if lock == "1":
                if paren == "(":
                    open.append(i)
                # greedily match close with open parenthesis, otherwise wildcard
                elif open:
                    open.pop()
                elif wildcard:
                    wildcard.pop()
                else:  # no "left" to match with "right"
                    return False
            else:
                wildcard.append(i)

        # close remaining open parentheses with wildcard
        while open and wildcard and open[-1] < wildcard[-1]:
            open.pop()
            wildcard.pop()

        # remaining wildcards should be even, otherwise we do not have a valid string
        return len(open) == 0 and len(wildcard) % 2 == 0


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "))()))", "010100",
        "()()", "0000",
        ")", "0",
        ")(", "10",
        "(((()(()", "10000011",  # "()()()()"
        "((((()(())", "1100000011",  # "(()()()())"
        "((((()(())", "1100000111",  # "(()()()())"
        "()))", "0010"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().canBeValid(*puzzle))
