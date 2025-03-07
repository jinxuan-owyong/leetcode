# 647. Palindromic Substrings

from utils import chunk


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        a palindrome can either be odd or even length
        if even: must have 2 same characters in the middle
        else:    start from a single character
        if s[i:j+1] is a palindrome, then if s[i-1] == s[j+1], s[i-1:j+2] is also a palindrome
        """

        def countPalindromes(i: int, j: int) -> int:
            if s[i] != s[j]:
                return 0

            count = 1
            while i-1 in range(len(s)) and j+1 in range(len(s)) and s[i-1] == s[j+1]:
                i, j = i-1, j+1
                count += 1  # only change from #5

            return count

        total = 0
        for i in range(len(s)):
            total += countPalindromes(i, i)
            if i > 0:
                total += countPalindromes(i-1, i)

        return total


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "abc",
        "aaa",
        "babad",
        "cbbd",
        "abca"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countSubstrings(*puzzle))
