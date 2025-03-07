# 5. Longest Palindromic Substring

from utils import chunk


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if s[i:j+1] is a palindrome, then s[i-1:j+2] is also a palindrome if s[i-1] == s[j+1]
        # the smallest possible palindrome is either s[i] or s[i:i+2] if s[i] == s[i+1]
        # dp[i] = max palindrome length from position i
        dp = [1] * len(s)  # since every character is a valid palindrome
        explore = []
        for i in range(len(s)-1):
            explore.append((i, i))
            if s[i] == s[i+1]:
                explore.append((i, i+1))
                dp[i] = 2  # other possible base case

        palindrome = s[0]
        for i, j in explore:
            # attempt to expand window outwards, only if the next left and right character are the same
            while i-1 in range(len(s)) and j+1 in range(len(s)) and s[i-1] == s[j+1]:
                i, j = i-1, j+1
            if j-i+1 > len(palindrome):
                palindrome = s[i:j+1]

        return palindrome


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "babad",
        "cbbd"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().longestPalindrome(*puzzle))
