# 739. Daily Temperatures

from utils import chunk
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        use a monotonic increasing stack to keep track of temperatures so far from the back
        store temperature indices in the stack to facilitate number of days calculation
        iterate temperatures in reverse order so that we have already accounted for future temperatures
        pop stack until top is greater than the current temperature
        """
        result = []
        stack = []

        for i in reversed(range(len(temperatures))):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                result.append(stack[-1] - i)
                stack.append(i)
            else:
                result.append(0)
                stack.append(i)

        result.reverse()
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [73, 74, 75, 71, 69, 72, 76, 73],
        [30, 40, 50, 60],
        [30, 60, 90],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().dailyTemperatures(*puzzle))
