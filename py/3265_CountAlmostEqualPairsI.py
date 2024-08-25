# 3265. Count Almost Equal Pairs I

from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def isAlmostEqual(a: int, b: int) -> bool:
            # swap is performed at most once
            if a == b:
                return True

            a, b = str(a), str(b)
            # edge case: use longer string to allow leading zero - "30", "3" situation
            if len(a) < len(b):
                a, b = b, a

            # O(N^2), but up to 10^6 -> 7 chars
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    swapped = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
                    if int(swapped) == int(b):
                        return True

            return False

        result = 0

        # O(N^2), up to 100 numbers
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if isAlmostEqual(nums[i], nums[j]):
                    result += 1

        return result


if __name__ == "__main__":
    puzzles = [
        [3, 12, 30, 17, 21],
        [1, 1, 1, 1, 1],
        [123, 231],
        [1234, 1324],
        [1234, 4321]
    ]
    for puzzle in puzzles:
        print(Solution().countPairs(puzzle))
