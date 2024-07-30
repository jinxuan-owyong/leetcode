# 2045. Second Minimum Time to Reach Destination

from typing import List
from collections import deque, defaultdict

# https://www.youtube.com/watch?v=2F7gwxfy1CU
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adjList = {u: [] for u in range(1, n+1)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        # perform BFS
        bfs = deque([1])
        currTime = 0
        lastVisitedAt = defaultdict(list)
        hasFoundMinCost = False
        while bfs:
            for _ in range(len(bfs)):
                u = bfs.popleft() 
                if u == n:
                    if hasFoundMinCost:
                        return currTime
                    hasFoundMinCost = True

                # note: there can be two or more paths of the 
                # same minimum weight leading up to node n
                for v in adjList[u]:
                    isFirstVisit = len(lastVisitedAt[v]) == 0
                    isValidSecondVisit = len(lastVisitedAt[v]) == 1 and lastVisitedAt[v][0] != currTime
                    if isFirstVisit or isValidSecondVisit:
                        bfs.append(v)
                        lastVisitedAt[v].append(currTime)
            
            # 0        1      2        3
            # green -> red -> green -> red -> ...
            isRed = ((currTime // change) % 2) == 1 
            if isRed:
                currTime += change - (currTime % change)
            currTime += time

if __name__ == "__main__":
    puzzles = [
        (5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5),
        (2, [[1, 2]], 3, 2),
    ]
    for puzzle in puzzles:
        print(Solution().secondMinimum(*puzzle))

"""
Runtime
1789
ms
Beats
87.42%
Memory
26.16
MB
Beats
93.38%
"""