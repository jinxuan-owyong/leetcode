# 271. Encode and Decode Strings

from utils import chunk
from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        serialized = ""
        for s in strs:
            serialized += f"{len(s)}#{s}"
        return serialized

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            j = s.index('#', i)
            size = int(s[i:j])
            j += 1
            strs.append(s[j:j+size])
            i = j+size
        return strs


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["neet", "code", "love", "you"],
        ["we", "say", ":", "yes"]
    ]
    for puzzle in chunk(puzzles, testSize):
        encoded = Solution().encode(*puzzle)
        decoded = Solution().decode(encoded)
        print(encoded, decoded, puzzle == decoded)
