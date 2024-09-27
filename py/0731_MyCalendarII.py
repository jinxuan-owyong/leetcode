# 731. My Calendar II

from utils import chunk


class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlapping = []

    def book(self, start: int, end: int) -> bool:
        s1, e1 = start, end

        # check if there are already 2 bookings overlapping with desired booking
        for s2, e2 in self.overlapping:
            if not (e1 <= s2 or e2 <= s1):
                return False

        # record overlapping area if desired booking overlaps with current booking(s)
        for s2, e2 in self.bookings:
            if not (e1 <= s2 or e2 <= s1):
                self.overlapping.append((max(s1, s2), min(e1, e2)))

        self.bookings.append((s1, e1))
        return True


if __name__ == "__main__":
    puzzles = [
        ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"],
        [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
        ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"],
        [[], [1, 2], [2, 3], [3, 4], [4, 5], [3, 5], [3, 6]]
    ]
    for words, prefixes in chunk(puzzles, 2):
        obj = eval(f'{words[0]}()')
        for word, prefix in zip(words[1:], prefixes[1:]):
            print(getattr(obj, word)(*prefix))
        print()
