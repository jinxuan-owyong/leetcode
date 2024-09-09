# 208. Implement Trie (Prefix Tree)


class TrieNode:
    def __init__(self):
        self.mapping = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.mapping:
                curr.mapping[c] = TrieNode()
            curr = curr.mapping[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.mapping:
                return False
            curr = curr.mapping[c]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.mapping:
                return False
            curr = curr.mapping[c]
        return True


if __name__ == "__main__":
    puzzles = [
        (["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
         [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]),
    ]
    for words, prefixes in puzzles:
        obj = Trie()
        for word, prefix in zip(words[1:], prefixes[1:]):
            print(getattr(obj, word)(prefix[0]))
        print()
