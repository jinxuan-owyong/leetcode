# 1813. Sentence Similarity III

from utils import chunk


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1

        words1, words2 = sentence1.split(), sentence2.split()

        i = -1
        while i < len(words1) - 1 and words1[i + 1] == words2[i + 1]:
            i += 1

        offset = len(words2) - len(words1)
        j = len(words1)
        while j > 0 and words1[j - 1] == words2[offset + j - 1]:
            j -= 1

        # i, j both point to words in the shorter sentence
        return i + 1 >= j


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "My name is Haley",
        "My Haley",
        "of",
        "A lot of words",
        "Eating right now",
        "Eating",
        "a",
        "a aa a"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().areSentencesSimilar(*puzzle))
