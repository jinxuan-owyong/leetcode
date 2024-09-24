# 3043. Find the Length of the Longest Common Prefix

from utils import chunk
from typing import List, Set


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode(-1)

    def insert(self, word: str):
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                node = TrieNode(c)
                curr.children[c] = node
                curr = node
        curr.isWord = True

    def hasPrefix(self, prefix: int) -> bool:
        curr = self.root
        for c in str(prefix):
            if c in curr.children:
                curr = curr.children[c]
            else:
                return ""
        return prefix


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def toTrie(nums: List[int]) -> Trie:
            trie = Trie()
            for word in map(str, nums):
                trie.insert(word)
            return trie

        def getPrefix(nums: List[int], trie: Trie) -> Set[int]:
            result = set()
            for num in nums:
                while num:
                    curr = trie.hasPrefix(num)
                    if curr:
                        result.add(curr)
                    num //= 10
            return result

        def size(n: int) -> int:
            count = 0
            while n:
                count += 1
                n //= 10
            return count

        trie1, trie2 = toTrie(arr1), toTrie(arr2)
        prefix1, prefix2 = getPrefix(arr1, trie2), getPrefix(arr2, trie1)

        # default value to return if no common prefixes
        result = 0
        for p in prefix1:
            # check if prefix is common
            if p in prefix2:
                result = max(result, size(p))

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 10, 100],
        [1000],
        [1, 2, 3],
        [4, 4, 4],
        [5655359, 5, 56],
        [56554, 5656]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().longestCommonPrefix(*puzzle))
