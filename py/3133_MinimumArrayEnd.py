# 3133. Minimum Array End

from utils import chunk


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """
        n = 3, x = 4
        given x is the bitwise AND of all n elements in the result array
        then all elements must have the same set bits as x, hence it is the first element
        x = 4 = 0b100
        to find the next (n - 1) values in the result array, the set bits that they contain 
        can be anything except what x has. in this case, we can use bits 1 and 0, since the
        numbers are increasing, the next possible values are 0b110 = 5 and 0b111 = 6.

        initial thought:
            using a starting value of curr = 0
            for i in range(n):
                result[i] = x | curr
                curr += 1

        above solution is only valid up to n = 5. when we reach result[4] = 0b111, we cannot 
        take curr = 0b100 since it will be equal to x -> hence it needs to be skipped

        n = 2, x = 7
        since 7 = 0b0111, the first unset bit is bit 3. to ensure that the next value has the 
        same set bits as x, then the next value is 0b1111 = 15

        if n is large or the next value is "far away", we have to perform repetitive work of 
        incrementing past unwanted bits e.g. curr = 0b111, but the next value is 0b1111

        instead, we look at the number of '0's that can be changed into '1's. we can replace the
        '0's of x with the binary representation of n - 1, which gives us the largest number
        for example, n = 14 = 0b1110 and x = 4 = 0b0000 0100
                      n - 1 = 0b1101
        we replace the last 4 '0's in x with 1101,
        x     =   0b0000 0100
        n - 1 =        1 1 01
        giving us 0b0001 1101
        """

        # O(64) time and space
        base = "{:064b}".format(x)
        insert = "{:0b}".format(n - 1)
        result = list(base)
        i = len(result) - 1
        j = len(insert) - 1

        while i >= 0 and j >= 0:
            if base[i] == '0':
                result[i] = insert[j]
                j -= 1
            i -= 1

        return int("".join(result), 2)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        3, 4,
        2, 7,
        9, 4,
        100_000_000, 100_000_000,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minEnd(*puzzle))
