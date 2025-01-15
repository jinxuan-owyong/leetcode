# 2429. Minimize XOR

from utils import chunk


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        the lowest possible value is 0
        to minimuse x ^ num1, x = ~num1 if there are no restrictions
        we greedily set the most significant bits to the same as num1 in x,
        first determine the number of set bits in both num1 and num2
        if both have the same count, then we can achieve minimum 0 using x = num1
        if num2 has more bits, set bits from least significant bits in num1
        if num1 has more bits, then we unset as many least significant bits in num1 as possible
        """
        N = 32  # max int bits

        def bits(n: int) -> int:
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        count1, count2 = bits(num1), bits(num2)
        result = num1  # default for count1 == count2
        i = 0
        if count1 < count2:
            while i < N and count1 < count2:
                if not result & (1 << i):
                    # set bit
                    result = result | (1 << i)
                    count1 += 1
                i += 1
        elif count1 > count2:
            # remove the last count1 - count2 bits in count1
            while i < N and count1 > count2:
                if result & (1 << i):
                    # clear bit
                    result = result & ~(1 << i)
                    count1 -= 1
                i += 1

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        3, 5,
        1, 12,
        25, 72,
        65, 84,
        79, 74,
        1, (1 << 10) - 1,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimizeXor(*puzzle))
