# 3016. Minimum Number of Pushes to Type Word II


from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        freq = sorted(count.items(), key=lambda x: -x[1])

        mapping = ["" for _ in range(10)]  # keypad 2 - 9
        i = 2
        for char, _ in freq:
            if i == 10:
                i = 2
            mapping[i] += char
            i += 1

        totalPushes = 0
        for keypad in mapping:
            for i, char in enumerate(keypad):
                # ith position = (i + 1) pushes
                totalPushes += count[char] * (i + 1)

        return totalPushes


if __name__ == "__main__":
    puzzles = [
        "abcde",
        "xyzxyzxyzxyz",
        "aabbccddeeffgghhiiiiii"
    ]
    for puzzle in puzzles:
        print(Solution().minimumPushes(puzzle))
