# 167. Two Sum II - Input Array Is Sorted

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            curr = numbers[i] + numbers[j]
            if curr == target:
                return [i + 1, j + 1]
            elif curr < target:
                i += 1
            else:
                j -= 1


if __name__ == "__main__":
    puzzles = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
        ([0, 0, 1], 0),
    ]
    for puzzle in puzzles:
        print(Solution().twoSum(*puzzle))

"""
Runtime
98
ms
Beats
89.10%
Memory
17.71
MB
Beats
20.66%
"""
