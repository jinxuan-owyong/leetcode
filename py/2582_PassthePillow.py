# 2582. Pass the Pillow

from utils import chunk


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """
        for every 2*(n-1) seconds, the pillow returns to the first person
        time = 10, n = 3
        1 -> 2 -> 3 -> 2 -> 1 (4 seconds)
        1 -> 2 -> 3 -> 2 -> 1 -> 2 -> 3 -> 2 -> 1 (8 seconds)
        1 -> 2 -> 3 -> 2 -> 1 -> 2 -> 3 -> 2 -> 1 -> 2 -> 3 (10 seconds)
        1 + time%(2*(n-1)) = 3

        time = 2, n = 3 has the same outcome
        1 -> 2 -> 3 (2 seconds) 
        (1 + time = 3)

        time = 3, n = 3 has the same outcome
        1 -> 2 -> 3 -> 2 (3 seconds) 
        (1 + time%(2*(n-1))

        """
        time %= 2*(n-1)
        if time < n:
            return 1 + time
        else:
            time -= n
            # count from the other direction
            return n - time - 1


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        4, 5,
        3, 2
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().passThePillow(*puzzle))
