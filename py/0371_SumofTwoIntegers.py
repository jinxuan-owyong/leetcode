# 371. Sum of Two Integers

from utils import chunk


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        implement full adder to add integers one by one

        full adder truth table
        a | b | carry_in | s | carry_out
        0 | 0 |    0     | 0 |     0
        1 | 0 |    0     | 1 |     0
        0 | 1 |    0     | 1 |     0
        0 | 0 |    1     | 1 |     0
        1 | 1 |    0     | 0 |     1
        0 | 1 |    1     | 0 |     1
        1 | 0 |    1     | 0 |     1
        1 | 1 |    1     | 1 |     1
        """

        i = 0
        carry = 0
        result = 0
        for i in range(32):
            x = (a >> i) & 1
            y = (b >> i) & 1

            # print(x, y, carry, "{0:b}".format(result))
            # sum is 1 only for 1 or 3 input bits
            # xor ensures that there is no output if only 2 inputs
            total = x ^ y ^ carry
            # a carry is generated for 1 + 1 + 0, 1 + 0 + 1 or 1 + 1 + 1
            # as long as there are 2 set bits it is generated
            carry = (x & y) | (carry & (x | y))

            result |= total << i

        # most significant bit is 1 -> negative number
        # set the 33rd bit onwards to 1 to get the correct binary
        # representation of negative numbers
        if (result >> 31) & 1:
            result |= -1 << 32

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        1, 2,
        2, 3,
        -2, -5
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().getSum(*puzzle))
