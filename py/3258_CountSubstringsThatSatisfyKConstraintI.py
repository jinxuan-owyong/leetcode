# 3258. Count Substrings That Satisfy K-Constraint I

from collections import Counter


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        result = 0

        for size in range(1, len(s) + 1):
            if size <= k:
                result += len(s) - size + 1
                continue

            i = 0
            j = i + size - 1
            count = Counter(s[i:j+1])

            # sliding window
            while j < len(s):
                if count["0"] <= k or count["1"] <= k:
                    result += 1

                count[s[i]] -= 1
                i += 1
                j += 1
                if j < len(s):
                    count[s[j]] += 1

        return result


if __name__ == "__main__":
    puzzles = [
        ("10101", 1),
        ("1010101", 2),
        ("11111", 5)
    ]
    for puzzle in puzzles:
        print(Solution().countKConstraintSubstrings(*puzzle))
