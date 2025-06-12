# 567. Permutation in String

from utils import chunk
from collections import Counter
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # using a fixed size sliding window, we can check if a permutation of
        # s1 exists in s2
        # after every iteration, perform O(26) check if permutation exists -> O(26*N)
        if len(s1) > len(s2):
            return False

        # O(26) check can be optimised by keeping track of the number of matched chars in window
        # each time the count in have "passes" the count in want, we in/decrement accordingly
        # the number will only change when this threshold is hit
        # then the string is a permutation when matches is equal to number of unique chars in s1
        matches = 0
        required = len(set(s1))
        want = Counter(s1)
        have = defaultdict(int)
        i = 0
        for j in range(len(s2)):  # O(N)
            have[s2[j]] += 1
            if have[s2[j]] == want[s2[j]]:
                matches += 1

            # shrink window to size of s1
            while (j-i+1) > len(s1):
                if have[s2[i]] == want[s2[i]]:
                    matches -= 1
                have[s2[i]] -= 1
                i += 1

            if matches == required:
                return True

        return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         # using a fixed size sliding window, we can check if a permutation of
#         # s1 exists in s2
#         # after every iteration, perform O(26) check if permutation exists -> O(26*N)
#         if len(s1) > len(s2):
#             return False

#         want = Counter(s1)
#         have = defaultdict(int)
#         i = 0
#         for j in range(len(s2)): # O(N)
#             have[s2[j]] += 1

#             # shrink window to size of s1
#             while (j-i+1) > len(s1):
#                 have[s2[i]] -= 1
#                 i += 1

#             hasPermutation = True
#             for c in want: # O(26)
#                 if have[c] < want[c]:
#                     hasPermutation = False

#             if hasPermutation:
#                 return True

#         return False


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
