# 1930. Unique Length-3 Palindromic Subsequences

from utils import chunk


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        intuition:
        find characters with same start i and end k
        we can form at most len(s[i+1:k]) palindromes
        use a hashset to keep track of the unique palindromes

        indices of each char: {'a': [0, 1, 4], 'b': [2], 'c': [3]}
        since we are looking for unique palindromes, we consider the first and last value in the list
        as any index in between will result in evaluating palindromes that have already been added

        optimisation:
        only keep track of the first and last indices for each character -> if there are >=2 then they will differ
        then we just need to iterate up to O(26) * O(N) = O(N)

        further improvement:
        scan for the same character from the start and end of a string respectively
        then we can skip the main set and just count the number of unique characters in s[i+1:k]
        since we know that the start and end characters are already unique
        """
        palindromes = set()
        same = {}
        for i, c in enumerate(s):
            if c in same:
                same[c][0] = min(same[c][0], i)
                same[c][1] = max(same[c][1], i)
            else:
                same[c] = [i, i]

        for key in same:
            if same[key][0] < same[key][1]:
                i, k = same[key][0], same[key][-1]
                for j in range(i+1, k):
                    palindromes.add(s[i] + s[j] + s[k])

        return len(palindromes)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "aabca",
        "adc",
        "bbcbaba"
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countPalindromicSubsequence(*puzzle))
