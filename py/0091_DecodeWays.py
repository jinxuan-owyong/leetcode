# 91. Decode Ways

from utils import chunk
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom up
        dp = [0] * (len(s)+1)
        dp[-1] = 1
        for i in reversed(range(len(s))):
            # check for 1-digit numbers
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]  # can only form new strings if 2-digit is present

            if i < len(s)-1 and 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]

        return dp[0]

        # # top-down recursive
        # cache = {}
        # def decode(i):
        #     if i in cache:
        #         return cache[i]
        #     elif i == len(s): # reach the end of the string
        #         return 1
        #     elif s[i] == '0': # leading zeroes are invalid
        #         return 0
        #     curr = decode(i+1)
        #     if 10 <= int(s[i:i+2]) <= 26: # 2-digit decode should be in the map
        #         curr += decode(i+2)
        #     cache[i] = curr
        #     return curr
        # return decode(0)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "12",
        "226",
        "06",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().numDecodings(*puzzle))
