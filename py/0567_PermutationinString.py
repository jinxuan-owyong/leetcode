# 567. Permutation in String

from utils import chunk
from collections import Counter
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # to find if s2 contains a permutation of s1
        i, j = 0, 0
        valid, curr = Counter(s1), defaultdict(int)

        def decrementKey(key: str):
            if key not in curr:
                return
            if curr[key] == 1:
                del curr[key]
            else:
                curr[key] -= 1

        while j < len(s2):
            # reset if incrementing a char causes it to be more than s1
            if s2[j] not in valid or curr[s2[j]] == valid[s2[j]]:
                decrementKey(s2[i])
                i += 1
                if j < i:
                    j = i
                while i < j and s2[i] not in curr:
                    decrementKey(s2[i])
                    i += 1
            else:
                curr[s2[j]] += 1
                j += 1

            if valid == curr:
                return True

        return False


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "ab",
        "eidbaooo",
        "ab",
        "eidboaoo",
        "abc",
        "bcba"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().checkInclusion(*puzzle))
