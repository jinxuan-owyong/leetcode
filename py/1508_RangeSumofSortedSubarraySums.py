# 1508. Range Sum of Sorted Subarray Sums


from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []

        for size in range(1, n + 1):
            curr = sum(nums[:size])
            result.append(curr)
            for start in range(1, n - size + 1):
                curr += nums[start + size - 1] - nums[start - 1]
                result.append(curr)

        result.sort()
        total = 0
        for i in range(left - 1, right):
            total += result[i]

        return int(total % (1E9 + 7))


if __name__ == "__main__":
    puzzles = [
        ([1, 2, 3, 4], 4, 1, 5),
        ([1, 2, 3, 4], 4, 3, 4),
        ([4, 1, 2, 3], 4, 1, 10)
    ]
    for puzzle in puzzles:
        print(Solution().rangeSum(*puzzle))

"""
Runtime
288
ms
Beats
25.66%
Memory
36.23
MB
Beats
80.53%
"""
