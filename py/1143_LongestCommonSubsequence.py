# 1143. Longest Common Subsequence

from utils import chunk


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        use 2 pointers to keep track of the progress for each string
        at each iteration, we can make 3 choices
        if both pointers have same char
            count the current char and check the remaining strings text1[i+1:] and text2[j+1:]
        otherwise 
            skip char in text1
            skip char in text2
        """
        cache = {}

        def helper(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(text1) or j == len(text2):
                return 0
            result = -1
            if text1[i] == text2[j]:
                result = 1 + helper(i+1, j+1)
            else:
                result = max(
                    helper(i+1, j),
                    helper(i, j+1)
                )
            cache[(i, j)] = result
            return result
        return helper(0, 0)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "abcde",
        "ace",
        "abc",
        "abc",
        "abc",
        "def",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().longestCommonSubsequence(*puzzle))
