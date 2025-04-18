# 38. Count and Say

from utils import chunk


class Solution:
    def countAndSay(self, n: int) -> str:
        def encode(s: str) -> str:
            result = ""
            count = 0
            curr = s[0]
            for i in range(len(s)):
                if s[i] != curr:
                    result += f"{count}{curr}"
                    curr, count = s[i], 1
                else:
                    count += 1
            return result + f"{count}{curr}"

        result = "1"
        for _ in range(n-1):
            result = encode(result)
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countAndSay(*puzzle))
