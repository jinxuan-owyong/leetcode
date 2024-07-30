# 69. Sqrt(x)


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low, high = 1, x // 2
        while low <= high:
            mid = ((high - low) // 2) + low
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return high


if __name__ == "__main__":
    puzzles = [4, 8, 0, 1, 234, 17289469123]
    for puzzle in puzzles:
        print(Solution().mySqrt(puzzle))

"""
Runtime
24
ms
Beats
99.29%
of users with Python3
Memory
16.52
MB
Beats
42.59%
of users with Python3
11
"""
