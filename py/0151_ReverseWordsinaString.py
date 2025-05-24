# 151. Reverse Words in a String

from utils import chunk


class Solution:
    def reverseWords(self, s: str) -> str:
        result = reversed([word for word in s.split(' ') if word])
        return ' '.join(result)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().reverseWords(*puzzle))
