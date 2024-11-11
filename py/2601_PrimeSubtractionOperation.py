# 2601. Prime Subtraction Operation

from utils import chunk
from typing import List
import bisect


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        """
        to obtain the smallest nums[i], we can use binary search to find the largest prime that is smaller than nums[i]
        in the first example, this will work since the prime closest to nums[0] and nums[1] happens to give us the ideal
        result: [4, 9, 6, 10] -> [4 - 3, 9 - 7, 6, 10]
        subtraction is only required if nums[i - 1] > nums[i], hence we iterate up to range(1, len(nums))

        by modifying nums[0] to 100, we can show that the largest prime approach does not work
        instead of taking 9 - 7, which will result in nums[0] > nums[1], we take 9 - 5 instead, suggesting an iterative 
        approach to check for the first prime smaller than nums[i] which yields nums[i - 1] < nums[i]
        [100, 9, 6, 10] -> [100 - 97, 9 - 5, 6, 10]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                  307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                  401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                  503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                  601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                  701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                  809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
                  907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

        def subtractPrimeWithMinimumResult(n: int, limit: int) -> int:
            if n <= 2:
                return n

            # find the first prime number p such that n - p > limit
            # bisect returns the index of the first prime >= n
            i = bisect.bisect_left(primes, n)
            if i == 0:
                return n - primes[i]
            else:
                i -= 1
            while i > 0 and (n - primes[i]) <= limit:
                i -= 1

            # in [100, 9, 6, 10], we want to avoid 6 - 2 since 9 - 5 has already occured
            return n - primes[i] if n - primes[i] > limit else n

        i = 1
        isSorted = True
        nums[0] = subtractPrimeWithMinimumResult(nums[0], 0)
        while i < len(nums) and isSorted:
            nums[i] = subtractPrimeWithMinimumResult(nums[i], nums[i - 1])
            isSorted = isSorted and nums[i - 1] < nums[i]
            i += 1

        return isSorted


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [4, 9, 6, 10],
        [6, 8, 11, 12],
        [5, 8, 3],
        [100, 9, 6, 10],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().primeSubOperation(*puzzle))
