from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True  # plus one operation
        for i in range(len(digits) - 1, -1, -1):
            temp = (carry + digits[i]) // 10
            digits[i] = (carry + digits[i]) % 10
            carry = temp
        if carry:
            return [1, *digits]
        return digits


"""
Runtime
32
ms
Beats
82.74%
of users with Python3
Memory
16.54
MB
Beats
39.78%
of users with Python3
8
"""
