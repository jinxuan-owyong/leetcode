# 2678. Number of Senior Citizens


from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        The first ten characters consist of the phone number of passengers.
        The next character denotes the gender of the person.
        The following two characters are used to indicate the age of the person.
        The last two characters determine the seat allotted to that person.
        """
        return sum(1 if int(x[11:13]) > 60 else 0 for x in details)


if __name__ == "__main__":
    puzzles = [
        ["7868190130M7522", "5303914400F9211", "9273338290F4010"],
        ["1313579440F2036", "2921522980M5644"]
    ]
    for puzzle in puzzles:
        print(Solution().countSeniors(puzzle))

"""
Runtime
45
ms
Beats
66.83%
Memory
16.46
MB
Beats
75.00%
"""
