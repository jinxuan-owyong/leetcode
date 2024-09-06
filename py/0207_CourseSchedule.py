# 207. Course Schedule

from utils import chunk
from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = defaultdict(list)
        # b is the pre-requisite of a
        for a, b in prerequisites:
            indegree[a] += 1
            adjList[b].append(a)

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        if len(queue) == 0:
            return False

        # bfs to number courses
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neighbour in adjList[curr]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        print(order)
        return sum(indegree) == 0


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        2,
        [[1, 0]],
        2,
        [[1, 0], [0, 1]],
        5,
        [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]],
        3,
        [[1, 0], [1, 2], [0, 1]],
        5,
        [[1, 4], [2, 4], [3, 1], [3, 2]]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().canFinish(*puzzle))
