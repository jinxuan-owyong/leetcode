# 273. Integer to English Words


class Solution:
    def numberToWords(self, num: int) -> str:
        onesAndTeens = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]
        HUNDRED, THOUSAND, MILLION, BILLION = "Hundred", "Thousand", "Million", "Billion"
        units = ["Unknown", THOUSAND, MILLION, BILLION]

        def tensToWords(num: int) -> str:
            if num < 20:
                return onesAndTeens[num]
            elif num % 10 == 0:
                return tens[num // 10]
            return f"{tens[num // 10]} {onesAndTeens[num % 10]}"

        def hundredsToWords(num: int) -> str:
            if num < 20:
                return onesAndTeens[num]
            elif num < 100:
                return tensToWords(num)
            elif num % 100 == 0:
                return f"{onesAndTeens[num // 100]} {HUNDRED}"
            return f"{onesAndTeens[num // 100]} {HUNDRED} {tensToWords(num % 100)}"

        if num == 0:
            return "Zero"

        result = None
        i = 0
        while num:
            currGroup = hundredsToWords(num % 1000)
            isSpecial = currGroup == "Zero"

            if isSpecial:
                while num % 1000 == 0:
                    i += 1
                    num //= 1000
                continue

            if i == 0 and (result is None or (not result and isSpecial)):
                result = currGroup
            elif result is None:
                result = f"{currGroup} {units[i]}"
            else:
                result = f"{currGroup} {units[i]} {result}"

            if not isSpecial:
                num //= 1000
                i += 1

        return result


if __name__ == "__main__":
    puzzles = [
        123,
        12345,
        1234567,
        123456789,
        2147483647,
        0,
        9,
        1,
        10,
        100,
        1_000,
        10_000,
        100_000,
        1_000_000,
        10_000_000,
        100_000_000,
        1_000_000_000,
        1_000_000_001,
        1_010_101_010
    ]
    for puzzle in puzzles:
        print(Solution().numberToWords(puzzle))
