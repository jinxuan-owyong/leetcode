# 212. Word Search II

from utils import chunk
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        t = Trie()
        for word in words:
            t.insert(word)

        # use dfs, making use of a trie to see if we should continue the search
        # same cell is only used once in a word, but can be used for multiple words
        # iterate through all cells in the grid as starting cells
        # if the direction we want to go in is a child of the trie, we can check in that direction
        def dfs(i, j, visited, node, result):
            if i not in range(ROWS) or \
                j not in range(COLS) or \
                (i, j) in visited or \
                    board[i][j] not in node.children:
                return

            node = node.children[board[i][j]]
            if node.word:
                result.add(node.word)

            visited.add((i, j))
            dfs(i-1, j, visited, node, result)
            dfs(i+1, j, visited, node, result)
            dfs(i, j-1, visited, node, result)
            dfs(i, j+1, visited, node, result)
            visited.remove((i, j))

        result = set()
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, set(), t.root, result)

        return list(result)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        ["oath", "pea", "eat", "rain"],
        [["a", "b"], ["c", "d"]],
        ["abcb"],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findWords(*puzzle))
