# 2191. Sort the Jumbled Numbers


from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapInt(val: int) -> int:
            result = 0
            for n in str(val):
                result *= 10
                result += mapping[int(n)]
            return result

        mappedValues = [(mapInt(num), idx, num)
                        for idx, num in enumerate(nums)]
        return [x[2] for x in sorted(mappedValues)]


if __name__ == "__main__":
    puzzles = [
        ([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123]),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ]
    for puzzle in puzzles:
        print(Solution().sortJumbled(*puzzle))

"""
Runtime
935
ms
Beats
82.06%
Memory
26.01
MB
Beats
27.17%
"""
