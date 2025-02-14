# 1352. Product of the Last K Numbers

from utils import chunk


class ProductOfNumbers:

    def __init__(self):
        self.window = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.window = [1]
        else:
            self.window.append(self.window[-1] * num)

    def getProduct(self, k: int) -> int:
        # when window has been cleared by 0, but is still a "valid" k value
        if k > len(self.window) - 1:
            return 0
        # using prefix multiplication we can get the last k product of numbers
        return int(self.window[-1] / self.window[-1-k])


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        ["ProductOfNumbers", "add", "add", "add", "add", "add",
            "getProduct", "getProduct", "getProduct", "add", "getProduct"],
        [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]
    ]
    for words, prefixes in chunk(puzzles, 2):
        obj = ProductOfNumbers()
        for word, prefix in zip(words[1:], prefixes[1:]):
            print(getattr(obj, word)(prefix[0]))
        print()
