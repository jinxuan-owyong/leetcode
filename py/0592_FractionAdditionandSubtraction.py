# 592. Fraction Addition and Subtraction

from typing import List
import math


class Solution:
    class Fraction:
        def __init__(self, numerator: int, denominator: int):
            self.numerator = numerator
            self.denominator = denominator

        def __str__(self):
            return f"{self.numerator}/{self.denominator}"

    def fractionAddition(self, expression: str) -> str:
        def getFractionTerm(start: int) -> List[int]:
            i = start
            while i < len(expression) and expression[i].isdigit():
                i += 1
            return int(expression[start:i]), i + 1

        # parse fractions from string
        fractions = []
        start = 1 if expression[0] == "-" else 0

        while start < len(expression):
            isNegative = start > 0 and expression[start - 1] == "-"
            numerator, start = getFractionTerm(start)
            if isNegative:
                numerator *= -1
            denominator, start = getFractionTerm(start)
            fractions.append(self.Fraction(numerator, denominator))

        def addFractions(a: self.Fraction, b: self.Fraction):
            # find LCM of the denominators
            lcm = math.lcm(a.denominator, b.denominator)

            aMultiplier = lcm // a.denominator
            bMultiplier = lcm // b.denominator

            numerator = (a.numerator * aMultiplier) + \
                (b.numerator * bMultiplier)
            # b.denominator * bMultiplier should yield the same result
            denominator = (a.denominator * aMultiplier)

            # find GCD of numerator and denominator to simplify the fraction
            gcd = math.gcd(numerator, denominator)
            return self.Fraction(numerator // gcd, denominator // gcd)

        result = fractions[0]
        for i in range(1, len(fractions)):
            result = addFractions(result, fractions[i])

        return str(result)


if __name__ == "__main__":
    puzzles = [
        "-1/2+1/2",
        "-1/2+1/2+1/3",
        "1/3-1/2",
        "1/10+1/12",
        "7/11-24/7",
        "2/1+1/2+1/6+1/24+1/120+1/720+1/5040+1/40320"
    ]
    for puzzle in puzzles:
        print(Solution().fractionAddition(puzzle))
