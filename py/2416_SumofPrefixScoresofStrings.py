# 2416. Sum of Prefix Scores of Strings

from utils import chunk
from typing import List


class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.children = {}
        self.isWord = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode(-1)

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
            curr.count += 1
        curr.isWord = True

    def countPrefixes(self, word: str) -> bool:
        count = 0
        curr = self.root
        # every word is a prefix of its own
        for c in word:
            curr = curr.children[c]
            count += curr.count
        return count


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return list(map(trie.countPrefixes, words))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["abc", "ab", "bc", "b"],
        ["abcd"],
        ["a" * i for i in range(10)]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().sumPrefixScores(*puzzle))
