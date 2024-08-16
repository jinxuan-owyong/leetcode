# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        result = 0
        curr = set()

        while j < len(s):
            if s[j] in curr:
                result = max(result, len(curr))
                while i < j and s[j] in curr:
                    curr.remove(s[i])
                    i += 1

            curr.add(s[j])
            j += 1

        return max(result, len(curr))


if __name__ == "__main__":
    puzzles = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        " ",
        "dvdf"
    ]
    for puzzle in puzzles:
        print(Solution().lengthOfLongestSubstring(puzzle))
