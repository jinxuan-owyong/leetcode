# 1233. Remove Sub-Folders from the Filesystem

from utils import chunk
from typing import List
from collections import deque


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isFirstFolder = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insertPath(self, path: str):
                curr = self.root
                for folder in path.split('/'):
                    if folder not in curr.children:
                        curr.children[folder] = TrieNode()
                    curr = curr.children[folder]
                curr.isFirstFolder = True

        trie = Trie()
        for path in folder:
            trie.insertPath(path[1:])

        # level order traversal to find first TrieNode with isFirstFolder = True
        # if False, then check children in next level
        parentFolders = []
        queue = deque([(trie.root, '')])

        while queue:
            for _ in range(len(queue)):
                node, path = queue.popleft()
                if node.isFirstFolder:
                    parentFolders.append(path)
                else:
                    for key in node.children:
                        queue.append((node.children[key], f'{path}/{key}'))

        return parentFolders


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"],
        ["/a", "/a/b/c", "/a/b/d"],
        ["/a/b/c", "/a/b/ca", "/a/b/d"],
        ["/a", "/a/b", "/c"],
        ["/b"]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().removeSubfolders(*puzzle))
