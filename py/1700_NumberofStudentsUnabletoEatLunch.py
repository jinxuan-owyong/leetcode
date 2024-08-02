# 1700. Number of Students Unable to Eat Lunch

from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        unable = 0
        served = 0
        while queue and sandwiches and unable < len(queue):
            if queue[0] == sandwiches[served]:
                served += 1
                queue.popleft()
                unable = 0
            else:
                queue.append(queue.popleft())
                unable += 1
        return len(queue)


if __name__ == "__main__":
    puzzles = [
        ([1, 1, 0, 0], [0, 1, 0, 1]),
        ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
    ]
    for puzzle in puzzles:
        print(Solution().countStudents(*puzzle))

"""
Runtime
37
ms
Beats
76.24%
Memory
16.53
MB
Beats
33.12%
"""
