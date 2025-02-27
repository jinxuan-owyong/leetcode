# 424. Longest Repeating Character Replacement

from utils import chunk
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        we only care about the count of the most frequent character
        the window cannot take anymore replacements (not the most frequent) if windowSize (j-i+1) - mostFreq == k
        """

        i = 0
        result = 0
        window = defaultdict[str](int)
        mostFreq = 0
        
        for j in range(len(s)):
            window[s[j]] += 1
            # we do not need to update mostFreq even when its decremented 
            # since it we will need a higher mostFreq to get a larger result
            mostFreq = max(mostFreq, window[s[j]])
            
            # check if window size is exceeded
            while (j-i+1) - mostFreq > k:
                window[s[i]] -= 1
                i += 1

            result = max(result, j-i+1)

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "ABAB",
        2,
        "AABABBA",
        1,
        "XYYX",
        2,
        "BAAA",
        0,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().characterReplacement(*puzzle))
