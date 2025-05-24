# 443. String Compression

from utils import chunk
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        result, i = 0, 0

        for j in range(len(chars)):
            # either last iteration or when not consecutive repeating
            if j == len(chars)-1 or chars[j+1] != chars[i]:
                # we only need to keep track of the length for width >= 2
                # incrementing result here keeps the first character
                chars[result] = chars[i]
                result += 1
                if (width := j-i+1) >= 2:
                    for d in str(width):
                        chars[result] = d
                        result += 1
                i = j+1
            # continue expanding window
            # else:

        # result is at the index 1 after compressed string, so return itself
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["a", "a", "b", "b", "c", "c", "c"],
        ["a"],
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
        ["a", "a", "a", "b", "b", "a", "a"],
    ]
    for puzzle in chunk(puzzles, testSize):
        i = Solution().compress(*puzzle)
        print(''.join(puzzle[0][:i]))
