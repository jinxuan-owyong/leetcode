# 860. Lemonade Change

from typing import List
from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billsOnHand = defaultdict(int)
        for bill in bills:
            if bill == 5:
                billsOnHand[5] += 1
            elif bill == 10 and billsOnHand[5] >= 1:
                billsOnHand[10] += 1
                billsOnHand[5] -= 1
            elif bill == 20 and billsOnHand[5] >= 1 and billsOnHand[10] >= 1:
                billsOnHand[20] += 1
                billsOnHand[10] -= 1
                billsOnHand[5] -= 1
            elif bill == 20 and billsOnHand[5] >= 3:
                billsOnHand[20] += 1
                billsOnHand[5] -= 3
            else:
                return False
        return True


if __name__ == "__main__":
    puzzles = [
        [5, 5, 5, 10, 20],
        [5, 5, 10, 10, 20],
        [5, 5, 10, 20],
        [10]
    ]
    for puzzle in puzzles:
        print(Solution().lemonadeChange(puzzle))
