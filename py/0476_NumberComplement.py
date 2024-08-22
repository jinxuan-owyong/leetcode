# 476. Number Complement

class Solution:
    def findComplement(self, num: int) -> int:
        mask, temp = 0, num
        while temp:
            mask = (mask << 1) | 1
            temp >>= 1

        return num ^ mask


if __name__ == "__main__":
    puzzles = [5, 1, 8]
    for puzzle in puzzles:
        print(Solution().findComplement(puzzle))
