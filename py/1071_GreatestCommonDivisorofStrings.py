# 1071. Greatest Common Divisor of Strings

from utils import chunk


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # for a string to divide another, they must have the same prefix
        # find the longest common prefix in both strings
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        def isDivisible(s, divisor):
            N, DIV = len(s), len(divisor)
            if N % DIV:
                return False
            i = 0
            while i < N and s[i:i+DIV] == divisor:
                i += DIV
            return i == N

        i = 0
        result = ""
        for i in range(len(str2)):
            if str1[i] == str2[i]:
                divisor = str1[:i+1]
                # the largest string x such that x divides both str1 and str2
                if isDivisible(str1, divisor) and isDivisible(str2, divisor):
                    result = divisor

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "ABCABC",
        "ABC",
        "ABABAB",
        "ABAB",
        "LEET",
        "CODE",
        "ABCABC",
        "ABCABCABC",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().gcdOfStrings(*puzzle))
