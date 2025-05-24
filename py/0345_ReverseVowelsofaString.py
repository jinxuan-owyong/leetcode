# 345. Reverse Vowels of a String

from utils import chunk


class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c): return c.lower() in 'aeiou'

        s = list(s)
        i, j = 0, len(s)-1
        while True:
            while i < len(s) and not isVowel(s[i]):
                i += 1
            while j >= 0 and not isVowel(s[j]):
                j -= 1
            if i >= j:
                break
            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1

        return ''.join(s)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "IceCreAm",
        "leetcode"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().reverseVowels(*puzzle))
