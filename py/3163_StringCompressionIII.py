# 3163. String Compression III

from utils import chunk


class Solution:
    def compressedString(self, word: str) -> str:
        curr = word[0]
        count = 0
        result = ""

        for i in range(len(word)):
            if count == 9 or word[i] != curr:
                result += f"{count}{curr}"
                curr = word[i]
                count = 0
            count += 1

        return result + f"{count}{curr}"


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "abcde",
        "aaaaaaaaaaaaaabb"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().compressedString(*puzzle))
