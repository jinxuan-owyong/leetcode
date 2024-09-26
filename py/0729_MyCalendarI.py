# 729. My Calendar I

from utils import chunk
from sortedcontainers import SortedSet


class MyCalendar:

    def __init__(self):
        # stores booking intervals: [[10, 19], [20, 29]]
        self.bookings = SortedSet()

    def book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings.add((start, end))
            return True

        i = self.bookings.bisect_left((start, end))
        # earliest booking made is after current
        if i == 0 and end <= self.bookings[0][0]:
            self.bookings.add((start, end))
            return True

        # desired start is larger than largest current start
        # or current position to insert at is after desired booking
        if i == len(self.bookings) or self.bookings[i][0] >= end:
            i -= 1

        if self.bookings[i][1] <= start:
            self.bookings.add((start, end))
            return True

        return False


if __name__ == "__main__":
    puzzles = [
        ["MyCalendar", "book", "book", "book"],
        [[], [10, 20], [15, 25], [20, 30]],
        ["MyCalendar", "book", "book", "book", "book"],
        [[], [2, 2], [4, 4], [6, 6], [1, 8]],
        ["MyCalendar", "book", "book", "book"],
        [[], [3, 3], [2, 2], [4, 4]],
        # ["MyCalendar", *(["book"] * 1000)],
        # [[], *[[i, i] for i in reversed(range(0, 1000))]]
    ]
    for words, prefixes in chunk(puzzles, 2):
        obj = eval(f'{words[0]}()')
        for word, prefix in zip(words[1:], prefixes[1:]):
            print(getattr(obj, word)(*prefix))
        print()
