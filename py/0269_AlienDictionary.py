# 269. Alien Dictionary

from utils import chunk
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        when sorting strings lexicographically, we compare the ordering of the first differing character
        for adjacent strings, we can find the first difference that it becomes an edge in the graph
        e.g. "hrn" and "hrf" differ at position 2, so n -> f
        similarly, "hrf" and "er" differ at position 0, so h -> e
        find the topological ordering among the characters using the above edges to get the answer
        """
        # initialise with all characters provided since if we start from a character with
        # no adjacent elements, there is no cycle along that path
        adjList = {}
        for word in words:
            for ch in word:
                if ch not in adjList:
                    # a character can be visited more than once
                    adjList[ch] = set()

        for i in range(1, len(words)):
            a, b = words[i-1], words[i]

            # input is invalid as it is not in lexicographical order
            m = min(len(a), len(b))
            if len(a) > len(b) and a[:m] == b[:m]:
                return ""

            j = 0
            for j in range(m):
                if a[j] != b[j]:
                    adjList[a[j]].add(b[j])
                    break

        # find topological ordering using dfs
        # a node can be visited more than once and not form a cycle
        # A -> B, B -> C, A -> C. so set node as being visited during dfs and clear at the end of the function call
        order = []
        visiting = {}
        # returns whether a cycle was detected

        def dfs(ch):
            if ch in visiting:
                # if True, currently being visited, otherwise already visited
                return visiting[ch]
            visiting[ch] = True
            for nei in adjList[ch]:
                # node is visited more than once in the same DFS branch -> cycle
                if dfs(nei):
                    return True

            visiting[ch] = False
            order.append(ch)
            return False

        for ch in adjList:
            if dfs(ch):
                return ""

        order.reverse()
        return "".join(order)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["z", "o"],
        ["hrn", "hrf", "er", "enn", "rfnn"],
        ["abc", "bcd", "cde"],
        ["wrt", "wrf", "er", "ett", "rftt"],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().foreignDictionary(*puzzle))
