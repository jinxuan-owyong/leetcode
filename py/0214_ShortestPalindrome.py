# 214. Shortest Palindrome

from utils import chunk


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        largest = 0

        for i in reversed(range(len(s))):
            # brute force: find the first valid palindrome s[:i+1]
            if s[:i+1] == s[:i+1][::-1]:
                largest = i
                break

        # reverse the chars after i and add them in front of s
        return s[largest + 1:][::-1] + s


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "aacecaaa",
        "abcd",
        "abbaa",
        "abba",
        "abab",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().shortestPalindrome(*puzzle))
