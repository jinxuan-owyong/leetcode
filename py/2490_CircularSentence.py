# 2490. Circular Sentence

from utils import chunk


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        for i in range(len(words)):
            prev, curr = words[i], words[(i + 1) % len(words)]
            if prev[-1] != curr[0]:
                return False

        return True


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "leetcode exercises sound delightful",
        "eetcode",
        "Leetcode is cool",
        "leetcode eats soul",
        "happy leetcode",
        "Leetcode",
        "I like Leetcode"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().isCircularSentence(*puzzle))
