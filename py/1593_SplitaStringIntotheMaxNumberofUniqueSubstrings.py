# 1593. Split a String Into the Max Number of Unique Substrings

from utils import chunk


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        """
        we use i and j to denote the start and end of the next substring we want to split
        at each decision point, we perform the following:
        1. split the substring and add it to the set, if adding it does not result in a duplicate
        2. extend the substring to see if it yields a better result
        there are no more substrings when j == len(s)
        uncomment the code below to see the substrings after splitting 
        """
        curr = set()
        # result = []

        def helper(i: int, j: int):
            # nonlocal result
            if j == len(s):
                # if len(curr) > len(result):
                #     result = curr.copy()
                return len(curr)

            substring = s[i:j + 1]
            split = 0

            if substring not in curr:
                curr.add(substring)
                split = helper(j + 1, j + 1)
                curr.remove(substring)

            extend = helper(i, j + 1)

            return max(split, extend)

        splits = helper(0, 0)
        # print(result) # for visualisation purposes
        return splits


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "ababccc",
        "aba",
        "aa",
        "aaaaaab",
        "aaaaaaa"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxUniqueSplit(*puzzle))
