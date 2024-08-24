# 564. Find the Closest Palindrome

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def evenResult(half: str) -> str:
            return str(half) + str(half)[::-1]

        def oddResult(half: str) -> str:
            return str(half) + str(half)[::-1][1:]

        isEven = len(n) % 2 == 0
        mid = (len(n) // 2) + (0 if isEven else 1)
        half = int(n[:mid])
        n = int(n)

        # all single digits are paliindromes
        if n < 10:
            return str(n - 1)

        for i in range(1, 18):
            # 10, 100, 1000, ...
            if n == (10 ** i):
                return str(n - 1)
            # 11, 101, 1001, ...
            elif n == (10 ** i) + 1:
                return str(n - 2)
            # 99, 999, 9999, ...
            elif n == (10 ** i) - 1:
                return str(n + 2)

        # in the remaining cases, the nearest palindrome is always (half - 1) mirrored
        if isEven:
            # if mirroring itself gives a lower value, we do not need to decrement the half
            increment = int(evenResult(half + 1))
            stay = int(evenResult(half))
            decrement = int(evenResult(half - 1))
        else:
            increment = int(oddResult(half + 1))
            stay = int(oddResult(half))
            decrement = int(oddResult(half - 1))

        values = [(abs(increment - n), increment),
                  (abs(decrement - n), decrement)]
        if stay != n:
            values.append((abs(stay - n), stay))

        return str(sorted(values)[0][1])


if __name__ == "__main__":
    puzzles = [
        "123",
        "1",
        "1234",
        "2",
        "5",
        "10",
        "999",
        "1000",
        "1001",
        "1002",
        "12120",
        "88"
    ]
    for puzzle in puzzles:
        print(Solution().nearestPalindromic(puzzle))
