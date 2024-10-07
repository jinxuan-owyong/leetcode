# 2696. Minimum String Length After Removing Substrings

from utils import chunk


class Solution:
    def minLength(self, s: str) -> int:
        def removeSubstring(st: str, sub: str):
            try:
                i = st.index(sub)
                return st[:i] + st[i+2:], True
            except:
                return st, False

        toRemove = True
        while toRemove:
            s, removedAB = removeSubstring(s, "AB")
            s, removedCD = removeSubstring(s, "CD")
            toRemove = removedAB or removedCD

        return len(s)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "ABFCACDB",
        "ACBBD",
        "HELLOACACDBDBWORLD"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minLength(*puzzle))
